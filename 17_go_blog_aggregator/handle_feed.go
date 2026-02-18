package main

import (
	"context"
	"fmt"
)

func handleAggregate(s *state, cmd command) error {
	if len(cmd.Args) != 0 {
		return fmt.Errorf("usage: %s", cmd.Name)
	}

	feedURL := "https://www.wagslane.dev/index.xml"

	feed, err := s.rssClient.FetchFeed(context.Background(), feedURL)
	if err != nil {
		return fmt.Errorf("error fetching feed: %v", err)
	}

	fmt.Print(feed)

	return nil
}
