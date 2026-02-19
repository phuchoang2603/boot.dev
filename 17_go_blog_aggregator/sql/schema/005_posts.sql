-- +goose Up
CREATE TABLE posts
(
    id           UUID PRIMARY KEY,
    created_at   timestamp NOT NULL,
    updated_at   timestamp NOT NULL,
    title        TEXT      NOT NULL,
    url          TEXT      NOT NULL UNIQUE,
    description  TEXT,
    published_at timestamp,
    feed_id      uuid      NOT NULL,
    FOREIGN KEY (feed_id) REFERENCES feeds (id) ON DELETE CASCADE
);

-- +goose Down
DROP TABLE posts;