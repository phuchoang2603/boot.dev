# Go Blog Aggregator (gator)

Small CLI for syncing RSS posts into a Postgres-backed store so you can explore feeds, users, and aggregates.

## Requirements

1. **Go 1.25+** – required to build and install the `gator` executable.
2. **Postgres** – create a database (default name `gator`) that the CLI can talk to via a connection URL. Example docker composition already assumes `POSTGRES_DB=gator`.

## Install the CLI

```bash
go install github.com/phuchoang2603/boot.dev/17_go_blog_aggregator@latest
```

This installs the `gator` binary into your `$GOBIN` or `$GOPATH/bin`. Make sure that directory is on your `PATH`.

## Configuration

`gator` reads its settings from `$HOME/.gatorconfig.json`. Create that file with at least the database URL and the user name you want to operate as.

```json
{
  "db_url": "postgres://postgres:postgres@localhost:5432/gator?sslmode=disable",
  "current_user_name": "felix"
}
```

Adjust `db_url` to point at your Postgres instance. After you successfully log in or register, the CLI will persist the `current_user_name` for future commands.

## Running the Program

Once you have Go, Postgres, and the config file set, invoke the CLI from your terminal.

```bash
gator <command> [arguments]
```

Commands include:

- `login <email> <password>` – authenticate an existing user.
- `register <name> <email> <password>` – create a new account.
- `reset <email>` – request a password reset link.
- `users` – list registered users.
- `addfeed <feed_url>` – add a new feed (requires login).
- `feeds` – show all tracked feeds.
- `follow <feed_id>` / `unfollow <feed_id>` – toggle following for the current user.
- `following` – list feeds you are subscribed to.
- `agg` – aggregate posts across feeds.
- `browse` – browse posts as the logged-in user.

Every command logs errors and exits non-zero so you can script the workflow if needed.
