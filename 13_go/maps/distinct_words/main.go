package main

import "strings"

func countDistinctWords(messages []string) int {
	distinctWords := make(map[string]struct{})

	for _, message := range messages {
		words := strings.FieldsSeq(strings.ToLower(message))
		for word := range words {
			distinctWords[word] = struct{}{}
		}
	}

	return len(distinctWords)
}
