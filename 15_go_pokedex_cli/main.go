package main

import (
	"time"

	"github.com/phuchoang2603/boot.dev/15_go_pokedex_cli/internal/pokeapi"
)

type config struct {
	next          *string
	previous      *string
	pokeapiClient pokeapi.Client
}

func main() {
	pokeClient := pokeapi.NewClient(5*time.Second, 10*time.Second)
	cfg := config{
		next:          nil,
		previous:      nil,
		pokeapiClient: pokeClient,
	}

	startRepl(&cfg)
}
