DROP TABLE users;

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
VALUES (3, 'John', 39, 'CA', 'Jjdev21', 'welovebootdev', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (4, 'Ram', 42, 'IN', 'Ram11c', 'thisSQLcourserocks', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (5, 'Hunter', 30, 'MX', 'Hdev92', 'iLoveB00Ts', FALSE);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (6, 'Allan', 27, 'US', 'Alires', 'backendDev', TRUE);

INSERT INTO users(name, age, country_code, username, password, is_admin)
VALUES ('Lance', 20, 'FR', 'LanChr', 'backendDev', FALSE);

INSERT INTO users(name, age, country_code, username, password, is_admin)
VALUES ('Tiffany', 28, 'US', 'Tifferoon', 'SQLrocks', TRUE);

INSERT INTO users(name, age, country_code, username, password, is_admin)
VALUES ('Lane', 27, 'IN', 'wagslane', 'update_me', TRUE);

INSERT INTO users(name, age, country_code, username, password, is_admin)
VALUES ('Darren', 15, 'CA', 'Dshan', 'greavesWasHere', FALSE);

/* return name and username for every user with
   password = 'backendDev', 'welovebootdev', 'SQLrocks' */
SELECT name, users.username
FROM users
WHERE password IN ('backendDev', 'welovebootdev', 'SQLrocks')
ORDER BY name;