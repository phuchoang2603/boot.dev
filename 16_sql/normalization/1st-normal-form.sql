CREATE TABLE companies
(
    id            integer PRIMARY KEY,
    name          TEXT    NOT NULL,
    num_employees INTEGER NOT NULL
);

PRAGMA TABLE_INFO('companies');