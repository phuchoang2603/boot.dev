-- +goose Up
CREATE TABLE refresh_tokens
(
    token      text PRIMARY KEY,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL,
    user_id    uuid      NOT NULL,
    expires_at timestamp NOT NULL,
    revoked_at timestamp,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- +goose Down
DROP TABLE refresh_tokens;