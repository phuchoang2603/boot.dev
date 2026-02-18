-- +goose Up
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL ,
    name TEXT UNIQUE not NULL
);

-- +goose Down
DROP TABLE users;