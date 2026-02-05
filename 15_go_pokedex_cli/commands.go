package main

import (
	"errors"
	"fmt"
	"os"
)

type cliCommand struct {
	name        string
	description string
	callback    func(*config) error
}

func getCommands() map[string]cliCommand {
	return map[string]cliCommand{
		"exit": {
			"exit",
			"Exit the Pokedex",
			commandExit,
		},
		"help": {
			name:        "help",
			description: "Displays a help message",
			callback:    commandHelp,
		},
		"map": {
			name:        "map",
			description: "Displays next 20 location areas",
			callback:    commandMap,
		},
		"mapb": {
			name:        "mapb",
			description: "Displays previous 20 location areas",
			callback:    commandMapb,
		},
	}
}

func commandExit(cfg *config) error {
	fmt.Println("Closing the Pokedex... Goodbye!")
	os.Exit(0)
	return nil
}

func commandHelp(cfg *config) error {
	fmt.Println("Welcome to the Pokedex!")
	fmt.Println("Usage:")

	for _, value := range getCommands() {
		fmt.Printf("%v: %v\n", value.name, value.description)
	}

	return nil
}

func commandMap(cfg *config) error {
	locationResp, err := cfg.pokeapiClient.GetLocationAreaResp(cfg.next)
	if err != nil {
		return err
	}

	cfg.next = locationResp.Next
	cfg.previous = locationResp.Previous

	for _, locationArea := range locationResp.Results {
		fmt.Println(locationArea.Name)
	}
	return nil
}

func commandMapb(cfg *config) error {
	if cfg.previous == nil {
		return errors.New("you're on the first page")
	}

	locationResp, err := cfg.pokeapiClient.GetLocationAreaResp(cfg.previous)
	if err != nil {
		return err
	}

	cfg.next = locationResp.Next
	cfg.previous = locationResp.Previous

	for _, locationArea := range locationResp.Results {
		fmt.Println(locationArea.Name)
	}
	return nil
}
