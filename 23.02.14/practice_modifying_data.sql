-- 문제 1
CREATE TABLE users (
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
);

-- 문제 2
INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES
	('Beemo', 'Jeong', 10000101, NULL, NULL, 'beemo@hphk.kr'),
	('Jieun', 'Lee', 19930516, 'Seoul', 'Korea', NULL),
    ('Dami', 'Kim', 19950409, 'Seoul', 'Korea', NULL),
    ('Kwangsoo', 'Lee', 19850714, 'Seoul', 'Korea', NULL);

-- 문제 3
INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES
	('Chimchak', 'Man', 19831205, 'Seoul', 'Korea', 'calmdownman@sandboxnetwork.net'),
	('Jinbae', 'Kim', 19831223, 'Seoul', 'Korea', '109ace@naver.com'),
    ('Dankun', 'Kim', 19830924, 'Incheon', 'Korea', '1983kej@naver.com'),
    ('Homin', 'Joo', 19810926, 'Yongin', 'Korea', 'joohomin@sandboxnetwork.net'),
    ('Poong', 'Kim', 19781212, 'Seoul', 'Korea', NULL);
    
-- 문제 4
UPDATE users
SET
	first_name = 'Sungbum',
	last_name = 'Ha',
    birthday = 19970623
WHERE
	userId = 2;

-- 문제 5
UPDATE users
SET country = 'Korea'
WHERE
	country IS NULL;

-- 문제 6
DELETE FROM users
WHERE
	first_name = 'Beemo';

-- 문제 7
DELETE FROM users
WHERE
	first_name = 'Kwangsoo'
	and last_name = 'Lee';

-- 문제 8
DELETE FROM users
ORDER BY
	created_at DESC,
	userId DESC
LIMIT 1;