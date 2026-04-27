-- name: CreateRefreshToken :one
INSERT INTO refresh_tokens (
    token, created_at, updated_at, user_id, expires_at, revoked_at
)
VALUES (
    $1,
    NOW(),
    NOW(),
    $2,
    NOW() + INTERVAL '60 days',
    NULL
)
RETURNING *;

-- name: RevokeRefreshToken :exec
UPDATE refresh_tokens
SET
    revoked_at = NOW(),
    updated_at = NOW()
WHERE
    token = $1
    AND expires_at > NOW();
