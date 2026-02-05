package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func cleanInput(text string) []string {
	loweredText := strings.ToLower(text)
	return strings.Fields(loweredText)
}

func startRepl() {
	scanner := bufio.NewScanner(os.Stdin)

	for {
		fmt.Print("Pokedex > ")

		scanner.Scan()
		words := cleanInput(scanner.Text())
		if len(words) == 0 {
			continue
		}

		command, ok := getCommands()[words[0]]
		if !ok {
			fmt.Println("Unknown command")
			continue
		} else {
			if err := command.callback(); err != nil {
				fmt.Fprintln(os.Stderr, err)
			}
		}

		if err := scanner.Err(); err != nil {
			fmt.Fprintln(os.Stderr, err)
		}
	}
}
