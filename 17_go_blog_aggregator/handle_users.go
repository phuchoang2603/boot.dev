package main

import "fmt"

func handlerLogin(s *state, cmd command) error {
	if len(cmd.Args) != 1 {
		return fmt.Errorf("usage: %s <username>", cmd.Name)
	}

	if err := s.config.SetUser(cmd.Args[0]); err != nil {
		return err
	}

	fmt.Printf("Logged in as %s\n", cmd.Args[0])

	return nil
}
