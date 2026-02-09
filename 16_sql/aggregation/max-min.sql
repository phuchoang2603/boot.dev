-- DROP TABLE users;

CREATE TABLE users
(
    id           INTEGER PRIMARY KEY,
    name         TEXT        NOT NULL,
    age          INTEGER     NOT NULL,
    country_code TEXT        NOT NULL,
    username     TEXT UNIQUE NOT NULL,
    password     TEXT        NOT NULL,
    is_admin     BOOLEAN
);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (1, 'David', 34, 'US', 'DavidDev', 'insertPractice', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (2, 'Samantha', 29, 'BR', 'Sammy93', 'addingRecords!', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (3, 'John', 19, 'CA', 'Jjdev21', 'welovebootdev', TRUE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (4, 'Ram', 42, 'IN', 'Ram11c', 'thisSQLcourserocks', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (5, 'Hunter', 30, 'US', 'Hdev92', 'backendDev', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (6, 'Allan', 27, 'US', 'Alires', 'iLoveB00tdev', TRUE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (7, 'Lance', 20, 'US', 'LanChr', 'b00tdevisbest', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (8, 'Tiffany', 28, 'US', 'Tifferoon', 'autoincrement', TRUE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (9, 'Lane', 27, 'US', 'wagslane', 'update_me', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (10, 'Darren', 15, 'CA', 'Dshan', 'found_me', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (11, 'Albert', 55, 'BR', 'BertDev', 'one_al_name', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (12, 'Alvin', 27, 'US', 'AlvinA27', 'easter_egg', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (13, 'Al', 39, 'JP', 'quickCoder', 'snake_case', FALSE);

-- return the oldest admin user
SELECT MAX(users.age) AS age
FROM users
WHERE is_admin = TRUE;

-- return the youngest US citizen
SELECT MIN(users.age) AS age
FROM users
WHERE country_code = 'US';
