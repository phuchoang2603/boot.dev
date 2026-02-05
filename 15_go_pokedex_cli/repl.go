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

func startRepl(cfg *config) {
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
			args := words[1:]
			if err := command.callback(cfg, args...); err != nil {
				fmt.Fprintln(os.Stderr, err)
			}
		}

		if err := scanner.Err(); err != nil {
			fmt.Fprintln(os.Stderr, err)
		}
	}
}
