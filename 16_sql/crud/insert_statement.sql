CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country_code TEXT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);

INSERT INTO users (
	id,
	name,
	age,
	country_code,
	username ,
	password,
	is_admin
) VALUES (
	1,
	'David',
	'34',
	'US',
	'DavidDev',
	'insertPractice',
	FALSE 
);

INSERT INTO users (
	id,
	name,
	age,
	country_code,
	username ,
	password,
	is_admin
) VALUES (
	2,
	'Samantha',
	'29',
	'BR',
	'Sammy93',
	'addingRecords!',
	FALSE 
);

SELECT * FROM users u ;