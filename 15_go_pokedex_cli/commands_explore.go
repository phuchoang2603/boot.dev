package main

import (
	"errors"
	"fmt"
)

func commandExplore(cfg *config, args ...string) error {
	if len(args) != 2 {
		return errors.New("no areas provided")
	}

	locationArea := args[1]

	fmt.Printf("Exploring %v\n", locationArea)
	locationResp, err := cfg.pokeapiClient.GetLocationInfo(locationArea)
	if err != nil {
		return err
	}

	pokemons := locationResp.PokemonEncounters
	fmt.Println("Found Pokemon:")
	for _, pokemon := range pokemons {
		fmt.Printf(" - %v\n", pokemon.Pokemon.Name)
	}

	return nil
}
