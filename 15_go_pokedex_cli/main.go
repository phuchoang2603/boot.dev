package main

import (
	"time"

	"github.com/phuchoang2603/boot.dev/15_go_pokedex_cli/internal/pokeapi"
)

type config struct {
	next          *string
	previous      *string
	pokeapiClient pokeapi.Client
	pokedex       map[string]pokeapi.Pokemon
}

func main() {
	pokeClient := pokeapi.NewClient(5*time.Second, 30*time.Minute)
	cfg := config{
		next:          nil,
		previous:      nil,
		pokeapiClient: pokeClient,
		pokedex:       make(map[string]pokeapi.Pokemon),
	}

	startRepl(&cfg)
}
