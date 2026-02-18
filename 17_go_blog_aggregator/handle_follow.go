package main

import (
	"context"
	"fmt"
	"time"

	"github.com/google/uuid"
	"github.com/phuchoang2603/boot.dev/17_go_blog_aggregator/internal/database"
)

func handleFollow(s *state, cmd command) error {
	if len(cmd.Args) != 1 {
		return fmt.Errorf("usage: %s <feed_url>", cmd.Name)
	}

	currentUser, err := s.db.GetUser(context.Background(), s.cfg.CurrentUserName)
	if err != nil {
		return fmt.Errorf("error fetching current user: %v", err)
	}

	feed, err := s.db.GetFeed(context.Background(), cmd.Args[0])
	if err != nil {
		return fmt.Errorf("error fetching feed: %v", err)
	}

	feedFollowParams := database.CreateFeedFollowParams{
		ID:        uuid.New(),
		CreatedAt: time.Now(),
		UpdatedAt: time.Now(),
		UserID:    currentUser.ID,
		FeedID:    feed.ID,
	}

	feedFollowRow, err := s.db.CreateFeedFollow(context.Background(), feedFollowParams)
	if err != nil {
		return fmt.Errorf("error creating feed follow: %v", err)
	}

	fmt.Printf("User %s is now following feed %s\n", feedFollowRow.UserName, feedFollowRow.FeedName)

	return nil
}

func handleFollowing(s *state, cmd command) error {
	if len(cmd.Args) != 0 {
		return fmt.Errorf("usage: %s", cmd.Name)
	}

	currentUser, err := s.db.GetUser(context.Background(), s.cfg.CurrentUserName)
	if err != nil {
		return fmt.Errorf("error fetching current user: %v", err)
	}

	followingList, err := s.db.GetFeedFollowsForUser(context.Background(), currentUser.Name)
	if err != nil {
		return fmt.Errorf("error fetching following list: %v", err)
	}

	fmt.Printf("User %s is following:\n", currentUser.Name)
	for _, follow := range followingList {
		fmt.Printf("- %s\n", follow.FeedName)
	}

	return nil
}
