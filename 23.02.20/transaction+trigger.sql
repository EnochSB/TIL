SET autocommit = 0;

CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)
);

START TRANSACTION;

INSERT INTO users (name)
VALUES ('james'), ('mary');

SELECT * FROM users;

-- ROLLBACK;
COMMIT;

SELECT * FROM users;

SET autocommit = 1;

-- ---------------------------------------------------

DROP TABLE articles;

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', current_time(), current_time());

SELECT * FROM articles;

DELIMITER //
CREATE TRIGGER myTrigger
	BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
    SET NEW.updatedAt = current_time();
End//
DELIMITER ;

SHOW TRIGGERS;

UPDATE articles
SET title = 'newTitle'
where id = 1;

-- ---------------------------------------------------

CREATE TABLE articlelogs (
	id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER myLog
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articlelogs (description, createdAt)
    VALUES ('글이 작성되었습니다.', current_time());
END//
DELIMITER ;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title2', current_time(), current_time());

SELECT * FROM articles;
SELECT * FROM articlelogs;

-- ---------------------------------------------------
DROP TRIGGER myLog;

DELIMITER //
CREATE TRIGGER myLog
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articlelogs (description, createdAt)
    VALUES (concat(NEW.id, '번 글이 작성되었습니다'), current_time());
END//
DELIMITER ;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title3', current_time(), current_time());

SELECT * FROM articles;
SELECT * FROM articlelogs;

-- ---------------------------------------------------

CREATE TABLE backupArticles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER backup
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO backupArticles (title, createdAt, updatedAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updatedAt);
END//
DELIMITER ;

DELETE FROM articles
WHERE id = 1;

SELECT * FROM articles;
SELECT * FROM backupArticles;