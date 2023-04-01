CREATE TABLE examples (
	examId INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examId)
);
--
SHOW COLUMNS FROM examples;
--
DROP TABLE examples;
--
ALTER TABLE
	examples
ADD
	country VARCHAR(100) NOT NULL;
    
--
ALTER TABLE examples
add age INT NOT NULL,
add address VARCHAR(100) NOT NULL;

--
ALTER TABLE examples
MODIFY
	address VARCHAR(50) NOT NULL;
    
--
ALTER TABLE examples
MODIFY lastName VARCHAR(10) NOT NULL,
MODIFY firstName VARCHAR(10) NOT NULL;

--
ALTER TABLE examples
CHANGE COLUMN
	country state VARCHAR(100) NOT NULL;
--
ALTER TABLE
	examples
DROP
	address;
    
--
ALTER TABLE examples
DROP state,
DROP age;
