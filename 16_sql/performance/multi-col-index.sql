DROP TABLE transactions;
CREATE TABLE transactions
(
    id           INTEGER PRIMARY KEY,
    user_id      INTEGER,
    recipient_id INTEGER,
    sender_id    INTEGER,
    amount       INTEGER
);

CREATE INDEX user_id_recipient_id_idx
    ON transactions (user_id, recipient_id);