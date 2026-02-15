DROP TABLE users;

CREATE TABLE users
(
    id    INTEGER PRIMARY KEY,
    email TEXT,
    name  TEXT,
    age   INTEGER
);

CREATE INDEX email_idx ON users (email);

SELECT *
FROM users;