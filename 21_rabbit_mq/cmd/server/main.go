package main

import (
	"fmt"
	"log"
	"os"

	"github.com/bootdotdev/learn-pub-sub-starter/internal/gamelogic"
	"github.com/bootdotdev/learn-pub-sub-starter/internal/pubsub"
	"github.com/bootdotdev/learn-pub-sub-starter/internal/routing"
	amqp "github.com/rabbitmq/amqp091-go"
)

func main() {
	amqpConnURL := os.Getenv("AMQP_URL")
	conn, err := amqp.Dial(amqpConnURL)
	if err != nil {
		log.Fatalf("Failed to connect to RabbitMQ: %v", err)
	}
	defer conn.Close()

	publishCh, err := conn.Channel()
	if err != nil {
		log.Fatalf("Failed to open a channel: %v", err)
	}

	if err := pubsub.SubscribeGob(
		conn,
		routing.ExchangePerilTopic,
		routing.GameLogSlug,
		routing.GameLogSlug+".*",
		pubsub.DurableQueue,
		handlerLog(),
	); err != nil {
		log.Fatalf("Failed to subscribe to game log messages: %v", err)
	}

	_, _, err = pubsub.DeclareAndBind(
		conn,
		routing.ExchangePerilDLX,
		routing.DeadLetterQueue,
		"",
		pubsub.DurableQueue,
	)
	if err != nil {
		log.Fatalf("Failed to declare and bind DLX queue: %v", err)
	}

	gamelogic.PrintServerHelp()

	for {
		words := gamelogic.GetInput()
		if len(words) == 0 {
			continue
		}

		switch words[0] {
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
			fmt.Printf("Unknown command: %s\n", words[0])
		}
	}
}
