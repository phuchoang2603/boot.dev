DROP TABLE users;

CREATE TABLE users
(
    id           INTEGER PRIMARY KEY,
    name         TEXT        NOT NULL,
    age_in_days  INTEGER     NOT NULL,
    country_code TEXT        NOT NULL,
    username     TEXT UNIQUE NOT NULL,
    password     TEXT        NOT NULL,
    is_admin     BOOLEAN
);

INSERT INTO users(name, age_in_days, country_code, username, password, is_admin)
VALUES ('David', 14560, 'US', 'DavidDev', 'insertPractice', FALSE);

INSERT INTO users(name, age_in_days, country_code, username, password, is_admin)
VALUES ('Samantha', 15560, 'BR', 'Sammy93', 'addingRecords!', FALSE);

INSERT INTO users(name, age_in_days, country_code, username, password, is_admin)
VALUES ('John', 10560, 'CA', 'Jjdev21', 'welovebootdev', FALSE);

INSERT INTO users(name, age_in_days, country_code, username, password, is_admin)
VALUES ('Ram', 4560, 'IN', 'Ram11c', 'thisSQLcourserocks', FALSE);

INSERT INTO users(name, age_in_days, country_code, username, password, is_admin)
VALUES ('Hunter', 20560, 'US', 'Hdev92', 'backendDev', FALSE);

INSERT INTO users(name, age_in_days, country_code, username, password, is_admin)
VALUES ('Allan', 560, 'US', 'Alires', 'iLoveB00tdev', TRUE);

INSERT INTO users(name, age_in_days, country_code, username, password, is_admin)
VALUES ('Lance', 17560, 'US', 'LanChr', 'b00tdevisbest', FALSE);

INSERT INTO users(name, age_in_days, country_code, username, password, is_admin)
VALUES ('Tiffany', 18560, 'US', 'Tifferoon', 'autoincrement', TRUE);

INSERT INTO users(name, age_in_days, country_code, username, password, is_admin)
VALUES ('Lane', 9560, 'US', 'wagslane', 'update_me', FALSE);

-- return all users who are more than 40 years old
SELECT *
FROM users
WHERE age_in_days > 40 * 365;