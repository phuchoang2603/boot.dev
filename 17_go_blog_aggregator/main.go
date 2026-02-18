package main

import (
	"database/sql"
	"log"
	"os"

	_ "github.com/lib/pq"
	"github.com/phuchoang2603/boot.dev/17_go_blog_aggregator/internal/config"
	"github.com/phuchoang2603/boot.dev/17_go_blog_aggregator/internal/database"
	"github.com/phuchoang2603/boot.dev/17_go_blog_aggregator/internal/rss"
)

type state struct {
	cfg       *config.Config
	db        *database.Queries
	rssClient *rss.Client
}

func main() {
	// Reading the configuration.
	cfg, err := config.Read()
	if err != nil {
		log.Fatalf("Error reading config: %v", err)
	}

	// Initialize the database connection.
	db, err := sql.Open("postgres", cfg.DBURL)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()
	dbQueries := database.New(db)

	// Initialize Rssfeed Client
	client := rss.NewClient()

	// Create the program state.
	programState := state{
		&cfg,
		dbQueries,
		client,
	}

	// Set up the command handlers.
	cmds := commands{
		make(map[string]func(*state, command) error),
	}

	cmds.register("login", handlerLogin)
	cmds.register("register", handlerRegister)
	cmds.register("reset", handlerReset)
	cmds.register("users", handlerUsers)

	cmds.register("agg", handleAggregate)
	cmds.register("addfeed", handleAddFeed)
	cmds.register("feeds", handleListFeeds)
	cmds.register("follow", handleFollow)
	cmds.register("following", handleFollowing)

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
