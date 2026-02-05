package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for {
		fmt.Print("Pokedex > ")

		for scanner.Scan() {
			line := scanner.Text()
			words := cleanInput(line)
			fmt.Printf("Your command was: %v\n", words[0])
			break
		}

		if err := scanner.Err(); err != nil {
			fmt.Fprintln(os.Stderr, err)
		}

	}
}
