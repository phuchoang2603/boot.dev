package pubsub

import (
	"encoding/json"
	"fmt"
	"log"

	amqp "github.com/rabbitmq/amqp091-go"
)

type AckType int

const (
	Ack AckType = iota
	NackRequeue
	NackDiscard
)

func SubscribeJSON[T any](
	conn *amqp.Connection,
	exchange,
	queueName,
	key string,
	queueType SimpleQueueType,
	handler func(T) AckType,
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

			ackType := handler(val)
			switch ackType {
			case Ack:
				msg.Ack(false)
				log.Printf("Message acknowledged: %s", string(msg.Body))
			case NackRequeue:
				msg.Nack(false, true)
				log.Printf("Message negatively acknowledged and requeued: %s", string(msg.Body))
			case NackDiscard:
				msg.Nack(false, false)
				log.Printf("Message negatively acknowledged and discarded: %s", string(msg.Body))
			}
		}
	}()

	return nil
}
