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

	username, err := gamelogic.ClientWelcome()
	if err != nil {
		log.Fatalf("Could not get username: %v", err)
	}
	queueName := routing.PauseKey + "." + username

	_, _, err = pubsub.DeclareAndBind(
		conn,
		routing.ExchangePerilDirect,
		queueName,
		routing.PauseKey,
		pubsub.TransientQueue,
	)
	if err != nil {
		log.Fatalf("Failed to declare and bind queue: %v", err)
	}

	gs := gamelogic.NewGameState(username)

	for {
		words := gamelogic.GetInput()
		if len(words) == 0 {
			continue
		}

		switch words[0] {
		case "spawn":
			if err := gs.CommandSpawn(words); err != nil {
				fmt.Println(err)
			}
		case "move":
			_, err := gs.CommandMove(words)
			if err != nil {
				fmt.Println(err)
			}
		case "status":
			gs.CommandStatus()
		case "help":
			gamelogic.PrintClientHelp()
		case "spam":
			fmt.Println("Spamming not allowed!")
		case "quit":
			gamelogic.PrintQuit()
			return
		default:
			fmt.Printf("Unknown command: %s\n", words[0])
		}

	}
}
