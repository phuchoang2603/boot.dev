DROP TABLE users;

CREATE TABLE users
(
    id                  INTEGER PRIMARY KEY,
    name                TEXT        NOT NULL,
    age                 INTEGER     NOT NULL,
    username            TEXT UNIQUE NOT NULL,
    password            TEXT        NOT NULL,
    bank_id             INTEGER,
    bank_name           TEXT,
    bank_routing_number INTEGER,
    is_admin            BOOLEAN
);

INSERT INTO users(name, age, username, password, is_admin, bank_id, bank_name, bank_routing_number)
VALUES ('David', 34, 'david.lang', 'secure1234', FALSE, 1, 'Central Savings', 123456789);

INSERT INTO users(name, age, username, password, is_admin, bank_id, bank_name, bank_routing_number)
VALUES ('Sam', 12, 'sam-show', 'nasjds134', FALSE, 2, 'Bank of Boots', 987654321);

INSERT INTO users(name, age, username, password, is_admin, bank_id, bank_name, bank_routing_number)
VALUES ('Lane', 19, 'wagslane', '2jk3bAkm', FALSE, 3, 'Metro Trust Bank', 456789123);

INSERT INTO users(name, age, username, password, is_admin, bank_id, bank_name, bank_routing_number)
VALUES ('Allan', 27, 'allan.jules', '243nldn', FALSE, 2, 'Bank of Boots', 987654321);

-- Create banks and user_banks table
CREATE TABLE banks
(
    id             integer PRIMARY KEY,
    name           text    NOT NULL,
    routing_number integer NOT NULL
);

CREATE TABLE users_banks
(
    user_id integer,
    bank_id integer,
    UNIQUE (user_id, bank_id)
);

-- Test
INSERT INTO banks(id, name, routing_number)
VALUES (1, 'Central Savings', 123456789);

INSERT INTO banks(id, name, routing_number)
VALUES (2, 'Bank of Boots', 987654321);

INSERT INTO banks(id, name, routing_number)
VALUES (3, 'Metro Trust Bank', 456789123);

INSERT INTO users_banks(user_id, bank_id)
VALUES (1, 1);

INSERT INTO users_banks(user_id, bank_id)
VALUES (1, 2);

INSERT INTO users_banks(user_id, bank_id)
VALUES (2, 2);

INSERT INTO users_banks(user_id, bank_id)
VALUES (2, 3);

INSERT INTO users_banks(user_id, bank_id)
VALUES (3, 3);

INSERT INTO users_banks(user_id, bank_id)
VALUES (4, 3);

SELECT *
FROM banks
WHERE id IN (SELECT bank_id
             FROM users_banks);