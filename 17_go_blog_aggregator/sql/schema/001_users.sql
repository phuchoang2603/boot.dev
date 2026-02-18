-- +goose Up
CREATE TABLE users (
    id UUID PRIMARY KEY,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL ,
    name TEXT UNIQUE NOT NULL
);

-- +goose Down
DROP TABLE users;