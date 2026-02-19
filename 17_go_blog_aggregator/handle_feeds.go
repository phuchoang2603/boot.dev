package main

import (
	"context"
	"fmt"
	"time"

	"github.com/google/uuid"
	"github.com/phuchoang2603/boot.dev/17_go_blog_aggregator/internal/database"
)

func handlerAggregate(s *state, cmd command) error {
	if len(cmd.Args) != 0 {
		return fmt.Errorf("usage: %s", cmd.Name)
	}

	feedURL := "https://www.wagslane.dev/index.xml"

	_, err := s.rssClient.FetchFeed(context.Background(), feedURL)
	if err != nil {
		return fmt.Errorf("error fetching feed: %v", err)
	}

	return nil
}

func handlerAddFeed(s *state, cmd command, currentUser database.User) error {
	if len(cmd.Args) != 2 {
		return fmt.Errorf("usage: %s <feed_name> <feed_url>", cmd.Name)
	}

	feedParams := database.CreateFeedParams{
		ID:        uuid.New(),
		CreatedAt: time.Now(),
		UpdatedAt: time.Now(),
		Name:      cmd.Args[0],
		Url:       cmd.Args[1],
		UserID:    currentUser.ID,
	}

	feed, err := s.db.CreateFeed(context.Background(), feedParams)
	if err != nil {
		return fmt.Errorf("error creating feed: %v", err)
	}

	feedFollowParams := database.CreateFeedFollowParams{
		ID:        uuid.New(),
		CreatedAt: time.Now(),
		UpdatedAt: time.Now(),
		UserID:    currentUser.ID,
		FeedID:    feed.ID,
	}

	if _, err := s.db.CreateFeedFollow(context.Background(), feedFollowParams); err != nil {
		return fmt.Errorf("error creating feed follow: %v", err)
	}

	fmt.Printf("Feed %s added successfully with URL %s\n", feed.Name, feed.Url)

	return nil
}

func handlerListFeeds(s *state, cmd command) error {
	if len(cmd.Args) != 0 {
		return fmt.Errorf("usage: %s", cmd.Name)
	}

	feedsRow, err := s.db.GetAllFeeds(context.Background())
	if err != nil {
		return fmt.Errorf("error fetching feeds: %v", err)
	}

	fmt.Printf("Total feeds: %d\n", len(feedsRow))

	for _, row := range feedsRow {
		fmt.Printf("%s at %s by %s\n", row.Name, row.Url, row.Username)
	}

	return nil
}
