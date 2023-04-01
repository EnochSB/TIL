-- 문제 1
SELECT
	employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;

-- 문제 2
SELECT
	customerNumber, officeCode, customers.city, offices.city
from customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 3
SELECT
	customerNumber, officeCode, customers.city, offices.city
from customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
-- 문제 4
SELECT
	customerNumber, officeCode, customers.city, offices.city
FROM customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
-- 문제 5
-- 문제2는 LEFT JOIN을 했기 때문에 기본적으로 기준 테이블의 모든 레코드를 출력하고 조인테이블은 그에 맞는 레코드만 출력한다. 따라서 해당 도시의 오피스가 없다면 NULL로 표시된다.
-- 문제3은 RIGHT JOIN을 했기 때문에 조인 테이블의 모든 레코드를 출력하고 기준 테이블의 레코드를 그에 맞게 출력한 결과가 나온다. 따라서 해당 도시의 customer가 없다면 NULL로 표시된다.
-- 문제4는 INNER JOIN을 했기 때문에 기준 테이블과 조인 테이블에서 기준으로하는 city가 일치하는 레코드만 결과로 나온다.

-- 문제 6
SELECT
	customerNumber, officeCode, customers.city, offices.city
from customers
LEFT JOIN offices
	ON customers.city = offices.city
UNION
SELECT
	customerNumber, officeCode, customers.city, offices.city
from customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 7
SELECT orderdetails.orderNumber, orderDate
FROM orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderNumber;

-- 문제 8
SELECT orderNumber, orderdetails.productCode, productName
FROM orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;
    
-- 문제 9
SELECT orderdetails.orderNumber, orderdetails.productCode, orderDate, productName
FROM orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;