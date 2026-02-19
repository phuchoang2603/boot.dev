package main

import (
	"context"
	"fmt"
	"time"

	"github.com/google/uuid"
	"github.com/phuchoang2603/boot.dev/17_go_blog_aggregator/internal/database"
)

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
		return fmt.Errorf("error creating user: %v", err)
	}

	if err := s.cfg.SetUser(username); err != nil {
		return fmt.Errorf("error setting user in config: %v", err)
	}

	printUser(userData)

	return nil
}

func handlerLogin(s *state, cmd command) error {
	if len(cmd.Args) != 1 {
		return fmt.Errorf("usage: %s <username>", cmd.Name)
	}

	username := cmd.Args[0]
	userData, err := s.db.GetUser(context.Background(), username)
	if err != nil {
		return fmt.Errorf("user %s does not exist", username)
	}

	if err := s.cfg.SetUser(username); err != nil {
		return fmt.Errorf("error setting user in config: %v", err)
	}

	printUser(userData)

	return nil
}

func handlerUsers(s *state, cmd command) error {
	if len(cmd.Args) != 0 {
		return fmt.Errorf("usage: %s", cmd.Name)
	}

	users, err := s.db.GetAllUsers(context.Background())
	if err != nil {
		return fmt.Errorf("error fetching users: %v", err)
	}

	for _, user := range users {
		if user.Name == s.cfg.CurrentUserName {
			fmt.Printf("* %v (current)\n", user.Name)
			continue
		}
		fmt.Printf("* %v\n", user.Name)
	}

	return nil
}

func handlerReset(s *state, cmd command) error {
	if len(cmd.Args) != 0 {
		return fmt.Errorf("usage: %s", cmd.Name)
	}

	if err := s.db.DeleteAllUsers(context.Background()); err != nil {
		return fmt.Errorf("error deleting users: %v", err)
	}

	return nil
}

func printUser(user database.User) {
	fmt.Printf(" * ID:      %v\n", user.ID)
	fmt.Printf(" * Name:    %v\n", user.Name)
}

func middlewareLoggedIn(handler func(s *state, cmd command, user database.User) error) func(*state, command) error {
	return func(s *state, cmd command) error {
		currentUser, err := s.db.GetUser(context.Background(), s.cfg.CurrentUserName)
		if err != nil {
			return err
		}
		return handler(s, cmd, currentUser)
	}
}
