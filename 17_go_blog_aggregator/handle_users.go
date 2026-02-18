package main

import (
	"context"
	"fmt"
	"time"

	"github.com/google/uuid"
	"github.com/phuchoang2603/boot.dev/17_go_blog_aggregator/internal/database"
)

func handlerLogin(s *state, cmd command) error {
	if len(cmd.Args) != 1 {
		return fmt.Errorf("usage: %s <username>", cmd.Name)
	}

	username := cmd.Args[0]

	if _, err := s.db.GetUser(context.Background(), username); err != nil {
		return fmt.Errorf("user %s does not exist", username)
	}

	if err := s.cfg.SetUser(username); err != nil {
		return err
	}

	fmt.Printf("Logged in as %s\n", username)

	return nil
}

func handlerRegister(s *state, cmd command) error {
	if len(cmd.Args) != 1 {
		return fmt.Errorf("usage: %s <username>", cmd.Name)
	}

	username := cmd.Args[0]

	userParams := database.CreateUserParams{
		ID:        uuid.New(),
		CreatedAt: time.Now(),
		UpdatedAt: time.Now(),
		Name:      username,
	}

	userData, err := s.db.CreateUser(context.Background(), userParams)
	if err != nil {
		return err
	}

	if err := s.cfg.SetUser(username); err != nil {
		return err
	}

	fmt.Printf("Registered and logged in as %s\n", username)
	fmt.Printf("User data: %+v\n", userData)

	return nil
}
