package pubsub

import (
	"bytes"
	"encoding/gob"
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
	return subscribe(conn, exchange, queueName, key, queueType, handler, func(data []byte) (T, error) {
		var val T
		err := json.Unmarshal(data, &val)
		return val, err
	})
}

func SubscribeGob[T any](
	conn *amqp.Connection,
	exchange,
	queueName,
	key string,
	queueType SimpleQueueType,
	handler func(T) AckType,
) error {
	return subscribe(conn, exchange, queueName, key, queueType, handler, func(data []byte) (T, error) {
		var val T
		buffer := bytes.NewBuffer(data)
		dec := gob.NewDecoder(buffer)
		err := dec.Decode(&val)
		return val, err
	})
}

func subscribe[T any](
	conn *amqp.Connection,
	exchange,
	queueName,
	key string,
	queueType SimpleQueueType,
	handler func(T) AckType,
	unmarshaller func([]byte) (T, error),
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
			val, err := unmarshaller(msg.Body)
			if err != nil {
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
