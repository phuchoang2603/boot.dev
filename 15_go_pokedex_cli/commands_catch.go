package main

import (
	"errors"
	"fmt"
	"math/rand"
)

func commandCatch(cfg *config, args ...string) error {
	if len(args) != 1 {
		return errors.New("no pokemons provided")
	}

	pokemonName := args[0]

	fmt.Printf("Throwing a Pokeball at %v...\n", pokemonName)
	pokemonInfo, err := cfg.pokeapiClient.GetPokemon(pokemonName)
	if err != nil {
		return err
	}

	if pokemonInfo.BaseExperience <= 0 {
		return errors.New("invalid pokemon level")
	}
	catchChance := rand.Intn(pokemonInfo.BaseExperience)
	threshold := 100

	if catchChance > threshold {
		return fmt.Errorf("%v escaped", pokemonName)
	} else {
		fmt.Printf("%v was caught!\n", pokemonName)
		fmt.Println("You may now inspect it with the inspect command")
		cfg.pokedex[pokemonName] = pokemonInfo
	}

	return nil
}
