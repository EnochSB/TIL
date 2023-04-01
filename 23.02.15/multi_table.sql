CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(50) NOT NULL,
    userId INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO users (name)
VALUES
	('권미자'),
    ('류준하'),
    ('정영식');

INSERT INTO articles (title, content, userId)
VALUES
	('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 3);

SELECT * FROM articles
INNER JOIN users
	ON articles.userId = users.id;
    
SELECT productCode, productName, textDescription
FROM products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;
    
SELECT orders.orderNumber, status, priceEach
from orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;
    
SELECT orders.orderNumber, status, sum(priceEach * quantityOrdered) as 'totalSales'
from orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
GROUP BY
	orderNumber;
    
SELECT contactFirstName, orderNumber, status
from customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber;
    
SELECT employeeNumber, firstName, customerNumber, contactFirstName
from customers
RIGHT JOIN employees
	ON employees.employeeNumber = customers.salesRepEmployeeNumber
WHERE
	customerNumber IS NULL;

SELECT * FROM users;
SELECT * FROM articles;
