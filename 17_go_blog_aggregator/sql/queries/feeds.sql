-- name: CreateFeed :one
INSERT INTO feeds(id, created_at, updated_at, name, url, user_id)
VALUES ($1,
        $2,
        $3,
        $4,
        $5,
        $6)
RETURNING *;

-- name: GetAllFeeds :many
SELECT name, url, (SELECT name FROM users WHERE users.id = feeds.user_id) AS username
FROM feeds;

-- name: GetFeed :one
SELECT *
FROM feeds
WHERE url = $1
LIMIT 1;

-- name: MarkFeedFetched :exec
UPDATE feeds
SET last_fetched_at = $1,
    updated_at = $1
WHERE feeds.id = $2;

-- name: GetNextFeedToFetch :one
SELECT *
FROM feeds
ORDER BY last_fetched_at ASC NULLS FIRST
LIMIT 1;