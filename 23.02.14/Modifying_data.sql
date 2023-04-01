CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
	createAt DATE NOT NULL,
    PRIMARY KEY (id)
);

-- 데이터 삽입
INSERT INTO articles (id, title, content, createAt)
VALUES (1, 'hello', 'world', 20000101);

-- 조회
SELECT *
FROM articles;

-- 여러 데이터 삽입
INSERT INTO articles (title, content, createAt)
VALUES
	('title1', 'content1', 19000101),
	('title2', 'content2', 18000101),
    ('title3', 'content3', 17000101);

-- 현재 날짜
INSERT INTO articles (title, content, createAt)
VALUES ('mytitle', 'mycontent', curdate());

-- 레코드 업데이트
UPDATE articles
SET title = 'newTitle'
where
	id = 1;
    
-- 레코드의 여러 필드 업데이트
UPDATE articles
SET title = 'newTitle2',
	content = 'newContent2'
where
	id = 2;
    
-- 모든 레코드의 필드 값 업데이트
UPDATE articles
set content = replace(content, 'content', 'TEST');

-- 1번 레코드 삭제
DELETE FROM articles
WHERE id = 1;
    
-- 최근 레코드 삭제
DELETE FROM articles
ORDER BY createAt DESC
LIMIT 2;