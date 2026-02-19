package main

import (
	"context"
	"database/sql"
	"fmt"
	"strconv"
	"time"

	"github.com/google/uuid"
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

	for _, item := range rssFeed.Channel.Item {
		parsedTime, err := time.Parse(time.RFC1123Z, item.PubDate)
		if err != nil {
			fmt.Printf("Error parsing publication date for item '%s': %v\n", item.Title, err)
			continue
		}

		if _, err := s.db.CreatePost(context.Background(), database.CreatePostParams{
			ID:        uuid.New(),
			CreatedAt: time.Now(),
			UpdatedAt: time.Now(),
			Title:     item.Title,
			Url:       item.Link,
			Description: sql.NullString{
				String: item.Description,
				Valid:  true,
			},
			PublishedAt: sql.NullTime{
				Time:  parsedTime,
				Valid: true,
			},
			FeedID: feed.ID,
		}); err != nil {
			fmt.Printf("Error creating post for item '%s': %v\n", item.Title, err)
			continue
		}

		fmt.Printf("Added post '%s' from feed '%s'\n", item.Title, feed.Url)
	}

	return nil
}

func handlerBrowse(s *state, cmd command, currentUser database.User) error {
	if len(cmd.Args) > 1 {
		return fmt.Errorf("usage: %s [number_of_posts]", cmd.Name)
	}

	if len(cmd.Args) == 0 {
		cmd.Args = append(cmd.Args, "2")
	}

	limit, err := strconv.Atoi(cmd.Args[0])
	if err != nil {
		return fmt.Errorf("error parsing number of posts: %v", err)
	}

	posts, err := s.db.GetPostsForUser(context.Background(), database.GetPostsForUserParams{
		Name:  currentUser.Name,
		Limit: int32(limit),
	})
	if err != nil {
		return fmt.Errorf("error fetching posts for user: %v", err)
	}

	for _, post := range posts {
		fmt.Printf("- %s\n", post.Title)
	}

	return nil
}
