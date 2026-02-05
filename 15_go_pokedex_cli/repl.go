package main

import "strings"

func cleanInput(text string) []string {
	loweredText := strings.ToLower(text)
	return strings.Fields(loweredText)
}
