package main

type Analytics struct {
	MessagesTotal     int
	MessagesFailed    int
	MessagesSucceeded int
}

type Message struct {
	Recipient string
	Success   bool
}

// don't touch above this line

func analyzeMessage(analytics *Analytics, message Message) {
	msgSuccess := message.Success
	analytics.MessagesTotal += 1

	if msgSuccess {
		analytics.MessagesSucceeded += 1
	} else {
		analytics.MessagesFailed += 1
	}
}
