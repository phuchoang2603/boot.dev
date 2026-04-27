-- name: CreateUser :one
INSERT INTO users (id, created_at, updated_at, email, hashed_password)
VALUES (gen_random_uuid(), now(), now(), $1, $2)
RETURNING *;

-- name: UpdateUser :one
UPDATE users
SET
    updated_at = now(),
    email = $2,
    hashed_password = $3
WHERE id = $1
RETURNING *;

-- name: UpdateChirpyRed :one
UPDATE users
SET
    updated_at = now(),
    is_chirpy_red = $2
WHERE id = $1
RETURNING *;

-- name: DeleteAllUsers :exec
DELETE
FROM users;

-- name: GetUserByEmail :one
SELECT *
FROM users
WHERE email = $1;

-- name: GetUserFromRefreshToken :one
SELECT u.*
FROM users u
JOIN refresh_tokens rt ON u.id = rt.user_id
WHERE
    rt.token = $1
    AND revoked_at IS NULL
    AND expires_at > now();
