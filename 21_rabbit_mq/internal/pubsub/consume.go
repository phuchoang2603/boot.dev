package pubsub

import (
	"encoding/json"
	"fmt"
	"log"

	amqp "github.com/rabbitmq/amqp091-go"
)

func SubscribeJSON[T any](
	conn *amqp.Connection,
	exchange,
	queueName,
	key string,
	queueType SimpleQueueType,
	handler func(T),
) error {
	subChan, queue, err := DeclareAndBind(
		conn,
		exchange,
		queueName,
		key,
		queueType,
	)
	if err != nil {
		return fmt.Errorf("failed to declare and bind queue: %w", err)
	}

	subDelChan, err := subChan.Consume(
		queue.Name,
		"",
		false,
		false,
		false,
		false,
		nil,
	)
	if err != nil {
		return fmt.Errorf("failed to consume from queue: %w", err)
	}

	go func() {
		defer subChan.Close()
		for msg := range subDelChan {
			var val T
			if err := json.Unmarshal(msg.Body, &val); err != nil {
				log.Printf("Failed to unmarshal message: %v", err)
				continue
			}
			handler(val)
			if err := msg.Ack(false); err != nil {
				log.Printf("Failed to acknowledge message: %v", err)
				continue
			}
		}
	}()

	return nil
}
