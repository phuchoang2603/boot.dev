-- +goose Up
CREATE TABLE feed_follows
(
    id         UUID PRIMARY KEY,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL,
    user_id    uuid      NOT NULL,
    feed_id    uuid      NOT NULL,
    UNIQUE (user_id, feed_id),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (feed_id) REFERENCES feeds (id) ON DELETE CASCADE
);

-- +goose Down
DROP TABLE feed_follows;

