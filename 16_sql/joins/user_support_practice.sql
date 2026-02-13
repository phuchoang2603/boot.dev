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
VALUES (13, 'Jason', 39, 'JP', 'quickCoder', 'snake_case', FALSE);

CREATE TABLE support_tickets
(
    id          INTEGER PRIMARY KEY,
    user_id     INTEGER NOT NULL,
    issue_type  TEXT    NOT NULL,
    description TEXT,
    created_at  DATE    NOT NULL
);

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (1, 3, 'Payment Failure', 'Transaction did not go through.', '2023-01-10');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (2, 3, 'Refund Request', 'Incorrect charge on account.', '2023-01-20');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (3, 6, 'Account Access', 'Couldnt log in :(', '2023-02-17');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (4, 3, 'Account Access', 'My password is not working!', '2023-02-16');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (5, 11, 'Account Access', 'My password was reset', '2023-02-25');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (6, 7, 'App Bug', 'HELP! I CANT GET SEE MY INBOX!!!', '2023-03-01');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (7, 3, 'Feature Request', 'You should build an AI bear to help on the app', '2023-03-01');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (8, 13, 'Account Access', 'i am gedding a unable to loggin errer', '2023-03-10');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (9, 13, 'Account Access', 'still gedding that err', '2023-03-15');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (10, 10, 'Account Suspension', 'frick u guys, I hate this ****** app', '2023-03-15');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (11, 11, 'Fraud Alert', 'I seem to be getting some suspicious payment requests', '2023-04-07');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (12, 13, 'Account Access', 'My password was reset', '2023-04-20');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (13, 7, 'Account Access', 'boots plz helb', '2023-04-21');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (14, 7, 'Payment Failure', 'I am unable to send my business invoices!', '2023-04-22');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (15, 3, 'Fraud Alert', 'getting some sketchy messages', '2023-05-15');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (16, 11, 'App Bug', 'boots is clearly a dog', '2023-05-24');

INSERT INTO support_tickets(id, user_id, issue_type, description, created_at)
VALUES (17, 11, 'Account Suspension', 'Please unsuspend my account!', '2023-05-25');

SELECT u.name, u.username, COUNT(st.id) AS support_ticket_count
FROM users u
         INNER JOIN support_tickets st ON u.id = st.user_id
WHERE st.issue_type != 'Account Access'
GROUP BY u.username
HAVING support_ticket_count > 1
ORDER BY support_ticket_count DESC;