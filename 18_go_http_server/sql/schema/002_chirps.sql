-- +goose Up
CREATE TABLE chirps
(
    id         uuid PRIMARY KEY,
    created_at timestamp NOT NULL,
    updated_at timestamp NOT NULL,
    body       text      NOT NULL,
    user_id    uuid      NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- +goose Down
DROP TABLE chirps;