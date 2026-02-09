DROP TABLE transactions;

CREATE TABLE transactions
(
    id             INTEGER PRIMARY KEY,
    user_id        INTEGER NOT NULL,
    recipient_id   INTEGER,
    sender_id      INTEGER,
    note           TEXT,
    amount         INTEGER,
    was_successful BOOLEAN
);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (1, 2, 'Testing lunch transaction!', 10.50, TRUE);

INSERT INTO transactions (user_id, recipient_id, note, amount, was_successful)
VALUES (2, 10, 'Thanks for lunch!', -9.56, TRUE);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (2, 2, 'Car lunch problems', 256.21, FALSE);

INSERT INTO transactions (user_id, recipient_id, note, amount, was_successful)
VALUES (2, 8, 'Happy birthday!!', -50, TRUE);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (3, 3, 'MTG Draft', 50, FALSE);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (3, 3, 'a lunch with the friends', -12.56, TRUE);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (3, 3, 'paying ya back for lunch', 12.22, FALSE);

INSERT INTO transactions (user_id, recipient_id, note, amount, was_successful)
VALUES (4, 6, 'lunch break', -24.89, TRUE);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (4, 4, 'thanks for lunch yesterday', 10.00, TRUE);

INSERT INTO transactions (user_id, recipient_id, note, amount, was_successful)
VALUES (4, 14, '5 buck pizza for lunch', -5.00, TRUE);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (4, 4, 'lunch was goooood thanks, man!', 47.42, TRUE);

INSERT INTO transactions (user_id, recipient_id, note, amount, was_successful)
VALUES (5, 4, 'lunch meetup, lets get together again soon.', -16.91, FALSE);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (6, 4, 'not sure how much lunch was, heres 20', 20.00, TRUE);

INSERT INTO transactions (user_id, recipient_id, note, amount, was_successful)
VALUES (6, 13, 'Happy birthday, sis! Lets get lunch soon.', -100.00, TRUE);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (5, 9, 'Payin ya back for lunch on friday', 13.21, TRUE);

INSERT INTO transactions (user_id, sender_id, note, amount, was_successful)
VALUES (5, 5, 'Lunch break with the boys', 22.40, TRUE);

-- return the total amount spent by each one on lunch when that balance > 20
SELECT transactions.sender_id, SUM(transactions.amount) AS balance
FROM transactions
WHERE sender_id IS NOT NULL
  AND was_successful = TRUE
  AND note LIKE '%lunch%'
GROUP BY transactions.sender_id
HAVING balance > 20
ORDER BY balance DESC;