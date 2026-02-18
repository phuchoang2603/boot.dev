-- name: CreateFeedFollow :one
WITH inserted_feed_follow AS (
    INSERT INTO feed_follows (id, created_at, updated_at, user_id, feed_id)
        VALUES ($1,
                $2,
                $3,
                $4,
                $5)
        RETURNING *)
SELECT inserted_feed_follow.*,
       feeds.name AS feed_name,
       users.name AS user_name
FROM inserted_feed_follow
         INNER JOIN feeds ON feeds.id = inserted_feed_follow.feed_id
         INNER JOIN users ON users.id = inserted_feed_follow.user_id;

-- name: GetFeedFollowsForUser :many
SELECT *, u.name AS user_name, f.name AS feed_name
FROM feed_follows ff
         INNER JOIN users u ON u.id = ff.user_id
         INNER JOIN feeds f ON f.id = ff.feed_id
WHERE u.name = $1;