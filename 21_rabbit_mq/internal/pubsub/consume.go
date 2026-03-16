package pubsub

import amqp "github.com/rabbitmq/amqp091-go"

func SubscribeJSON[T any](
	conn *amqp.Connection,
	exchange,
	queueName,
	key string,
	queueType SimpleQueueType,
	handler func(T),
) error {
}
