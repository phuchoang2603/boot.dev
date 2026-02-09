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
VALUES (1, 'David', 34, 'US', 'DavidDev', 'insertPractice', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (2, 'Samantha', 29, 'BR', 'Sammy93', 'addingRecords!', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (3, 'John', 57, 'CA', 'Jjdev21', 'welovebootdev', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (4, 'Ram', 42, 'IN', 'Ram11c', 'thisSQLcourserocks', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (5, 'Rain', 14, 'IN', 'Ram11c76', 'loveThePass', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (6, 'Hunter', 72, 'US', 'Hdev92', 'backendDev', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (7, 'Allan', 27, 'US', 'Alires', 'iLoveB00tdev', true);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (8, 'Lance', 20, 'US', 'LanChr', 'b00tdevisbest', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (9, 'Tiffany', 15, 'US', 'Tifferoon', 'autoincrement', true);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (10, 'Lane', 27, 'US', 'wagslane', 'update_me', true);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (11, 'Darren', 15, 'CA', 'Dshan', 'found_me', false);

/* Return every user with additional column that shows the discount percentage they are eligible for
   based on their age or country_code */
SELECT name,
       age,
       country_code,
       iif(age > 55 or country_code = 'CA', 10, 0) as discount_percent
from users;
