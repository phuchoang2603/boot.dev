-- +goose Up
CREATE TABLE feeds (
    id UUID PRIMARY KEY,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL ,
    name TEXT UNIQUE NOT NULL,
    url TEXT UNIQUE NOT NULL ,
    user_id uuid NOT NULL ,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- +goose Down
DROP TABLE feeds;

