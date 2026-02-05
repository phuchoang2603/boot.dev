package main

import (
	"errors"
	"fmt"
)

func commandMap(cfg *config, args ...string) error {
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

func commandMapb(cfg *config, args ...string) error {
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
