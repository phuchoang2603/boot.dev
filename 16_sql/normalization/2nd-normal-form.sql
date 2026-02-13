DROP TABLE users;
DROP TABLE companies;

CREATE TABLE users
(
    id   INTEGER PRIMARY KEY,
    name TEXT    NOT NULL,
    age  INTEGER NOT NULL
);

CREATE TABLE companies
(
    id            INTEGER PRIMARY KEY,
    name          TEXT    NOT NULL,
    num_employees INTEGER NOT NULL,
    revenue       INTEGER
);

CREATE TABLE users_companies
(
    user_id    INTEGER,
    company_id INTEGER,
    UNIQUE (user_id, company_id)
);

PRAGMA TABLE_INFO('companies');
