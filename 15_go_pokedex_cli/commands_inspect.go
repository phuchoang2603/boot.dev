package main

import (
	"errors"
	"fmt"
)

func commandInspect(cfg *config, args ...string) error {
	if len(args) != 1 {
		return errors.New("no pokemons provided")
	}

	pokemonName := args[0]

	pokemonInfo, isCaught := cfg.pokedex[pokemonName]
	if !isCaught {
		return errors.New("you have not caught that pokemon")
	} else {
		fmt.Printf("Name: %v\n", pokemonInfo.Name)
		fmt.Printf("Height: %v\n", pokemonInfo.Height)
		fmt.Printf("Weight: %v\n", pokemonInfo.Weight)
		fmt.Println("Stats:")
		for _, stat := range pokemonInfo.Stats {
			fmt.Printf("  -%v: %v\n", stat.Stat.Name, stat.BaseStat)
		}
		fmt.Println("Types:")
		for _, pType := range pokemonInfo.Types {
			fmt.Printf("  -%v\n", pType.Type.Name)
		}
	}

	return nil
}
