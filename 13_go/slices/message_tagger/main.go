package main

import (
	"strings"
)

type sms struct {
	id      string
	content string
	tags    []string
}

func tagMessages(messages []sms, tagger func(sms) []string) []sms {
	for i, msg := range messages {
		messages[i].tags = tagger(msg)
	}

	// fmt.Println(messages)
	return messages
}

func tagger(msg sms) (tags []string) {
	if strings.Contains(strings.ToLower(msg.content), "urgent") {
		tags = append(tags, "Urgent")
	}

	if strings.Contains(strings.ToLower(msg.content), "sale") {
		tags = append(tags, "Promo")
	}

	// fmt.Println(tags)
	return
}
