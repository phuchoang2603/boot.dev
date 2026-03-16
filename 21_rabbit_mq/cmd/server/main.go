package main

import (
	"fmt"
	"log"

	"github.com/bootdotdev/learn-pub-sub-starter/internal/gamelogic"
	"github.com/bootdotdev/learn-pub-sub-starter/internal/pubsub"
	"github.com/bootdotdev/learn-pub-sub-starter/internal/routing"
	amqp "github.com/rabbitmq/amqp091-go"
)

func main() {
	const amqpConnURL = "amqp://guest:guest@localhost:5672/"
	conn, err := amqp.Dial(amqpConnURL)
	if err != nil {
		log.Fatalf("Failed to connect to RabbitMQ: %v", err)
	}
	defer conn.Close()

	publishCh, err := conn.Channel()
	if err != nil {
		log.Fatalf("Failed to open a channel: %v", err)
	}

	gamelogic.PrintServerHelp()

	for {
		inputs := gamelogic.GetInput()
		if len(inputs) == 0 {
			continue
		}

		switch inputs[0] {
		case "pause":
			fmt.Println("Pausing game...")
			pubsub.PublishJSON(
				publishCh,
				routing.ExchangePerilDirect,
				routing.PauseKey,
				routing.PlayingState{
					IsPaused: true,
				},
			)
		case "resume":
			fmt.Println("Resuming game...")
			pubsub.PublishJSON(
				publishCh,
				routing.ExchangePerilDirect,
				routing.PauseKey,
				routing.PlayingState{
					IsPaused: false,
				},
			)
		case "quit":
			fmt.Println("Quitting game...")
			return
		case "help":
			gamelogic.PrintServerHelp()
		default:
			fmt.Printf("Unknown command: %s\n", inputs[0])
		}
	}
}
