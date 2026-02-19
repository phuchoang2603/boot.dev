package main

import (
	"context"
	"database/sql"
	"fmt"
	"time"

	"github.com/phuchoang2603/boot.dev/17_go_blog_aggregator/internal/database"
)

func handlerAggregate(s *state, cmd command) error {
	if len(cmd.Args) != 1 {
		return fmt.Errorf("usage: %s <time_between_reqs>", cmd.Name)
	}

	duration, err := time.ParseDuration(cmd.Args[0])
	if err != nil {
		return fmt.Errorf("error parsing duration: %v", err)
	}

	fmt.Printf("Collecting feeds every %s ...\n", cmd.Args[0])

	ticker := time.Tick(duration)
	for range ticker {
		scrapeFeeds(s)
	}

	return nil
}

func scrapeFeeds(s *state) error {
	feed, err := s.db.GetNextFeedToFetch(context.Background())
	if err != nil {
		return fmt.Errorf("error fetching next feed to aggregate: %v", err)
	}

	if err := s.db.MarkFeedFetched(context.Background(), database.MarkFeedFetchedParams{
		LastFetchedAt: sql.NullTime{Time: time.Now(), Valid: true},
		ID:            feed.ID,
	}); err != nil {
		return fmt.Errorf("error marking feed as fetched: %v", err)
	}

	rssFeed, err := s.rssClient.FetchFeed(context.Background(), feed.Url)
	if err != nil {
		return fmt.Errorf("error fetching feed from URL: %v", err)
	}

	fmt.Printf("Feed Title: %s\n", rssFeed.Channel.Title)

	for _, item := range rssFeed.Channel.Item {
		fmt.Printf(" - %s\n", item.Title)
	}

	return nil
}
