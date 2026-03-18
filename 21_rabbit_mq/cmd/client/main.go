package main

import (
	"fmt"
	"log"
	"strconv"
	"time"

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

	username, err := gamelogic.ClientWelcome()
	if err != nil {
		log.Fatalf("Could not get username: %v", err)
	}

	gs := gamelogic.NewGameState(username)

	if err = pubsub.SubscribeJSON(
		conn,
		routing.ExchangePerilDirect,
		routing.PauseKey+"."+gs.GetUsername(),
		routing.PauseKey,
		pubsub.TransientQueue,
		handlerPause(gs),
	); err != nil {
		log.Fatalf("Failed to subscribe to pause messages: %v", err)
	}

	if err = pubsub.SubscribeJSON(
		conn,
		routing.ExchangePerilTopic,
		routing.ArmyMovesPrefix+"."+gs.GetUsername(),
		routing.ArmyMovesPrefix+".*",
		pubsub.TransientQueue,
		handlerMove(gs, publishCh),
	); err != nil {
		log.Fatalf("Failed to subscribe to move messages: %v", err)
	}

	if err = pubsub.SubscribeJSON(
		conn,
		routing.ExchangePerilTopic,
		routing.WarRecognitionsPrefix,
		routing.WarRecognitionsPrefix+"."+gs.GetUsername(),
		pubsub.DurableQueue,
		handlerWar(gs, publishCh),
	); err != nil {
		log.Fatalf("Failed to subscribe to war messages: %v", err)
	}

	for {
		words := gamelogic.GetInput()
		if len(words) == 0 {
			continue
		}

		switch words[0] {
		case "spawn":
			if err := gs.CommandSpawn(words); err != nil {
				fmt.Println(err)
				continue
			}
		case "move":
			mv, err := gs.CommandMove(words)
			if err != nil {
				fmt.Println(err)
				continue
			}
			if err := pubsub.PublishJSON(
				publishCh,
				routing.ExchangePerilTopic,
				routing.ArmyMovesPrefix+"."+mv.Player.Username,
				mv,
			); err != nil {
				fmt.Printf("error: %s\n", err)
				continue
			}
			fmt.Printf("Moved %v units to %s\n", len(mv.Units), mv.ToLocation)
		case "status":
			gs.CommandStatus()
		case "help":
			gamelogic.PrintClientHelp()
		case "spam":
			if len(words) != 2 {
				fmt.Println("usage: spam <n>")
				continue
			}
			n, err := strconv.Atoi(words[1])
			if err != nil {
				fmt.Printf("error: %s is not a valid number\n", words[1])
				continue
			}

			for range n {
				if err := pubsub.PublishGob(
					publishCh,
					routing.ExchangePerilTopic,
					routing.GameLogSlug+"."+gs.GetUsername(),
					routing.GameLog{
						CurrentTime: time.Now(),
						Message:     gamelogic.GetMaliciousLog(),
						Username:    gs.GetUsername(),
					},
				); err != nil {
					fmt.Printf("Failed to publish malicious log: %v\n", err)
					continue
				}
			}
		case "quit":
			gamelogic.PrintQuit()
			return
		default:
			fmt.Printf("Unknown command: %s\n", words[0])
		}

	}
}
