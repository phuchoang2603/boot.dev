package main

import (
	"log"
	"os"

	"github.com/phuchoang2603/boot.dev/17_go_blog_aggregator/internal/config"
)

type state struct {
	config *config.Config
}

func main() {
	cfg, err := config.Read()
	if err != nil {
		log.Fatalf("Error reading config: %v", err)
	}

	programState := state{
		&cfg,
	}

	cmds := commands{
		make(map[string]func(*state, command) error),
	}

	cmds.register("login", handlerLogin)

	args := os.Args
	if len(args) < 2 {
		log.Fatalf("Usage: <command> [arguments...]")
	}

	c := command{
		Name: args[1],
		Args: args[2:],
	}

	if err := cmds.run(&programState, c); err != nil {
		log.Fatal(err)
	}
}
