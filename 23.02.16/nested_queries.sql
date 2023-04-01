SELECT customerNumber, amount FROM payments
WHERE amount = (SELECT MAX(amount) FROM payments);

SELECT lastName, firstName
FROM employees
WHERE officeCode in (SELECT officeCode FROM offices WHERE country = 'USA');

SELECT * FROM customers;

SELECT * FROM orders;

SELECT customerName
FROM customers
WHERE customerNumber NOT IN (SELECT customerNumber FROM orders);

SELECT payments.customerNumber, amount, contactFirstName
FROM payments
INNER JOIN customers USING (customerNumber)
WHERE amount = (SELECT max(amount) FROM payments);

SELECT customerNumber, customerName
FROM customers
WHERE EXISTS (SELECT * FROM orders WHERE customers.customerNumber = orders.customerNumber);

SELECT employeeNumber, firstName, lastName
FROM employees
WHERE
	EXISTS (
		SELECT officeCode
        FROM offices
        WHERE city = 'Paris' AND
        employees.officeCode = offices.officeCode
);

SELECT contactFirstName, creditLimit,
	CASE
		WHEN creditLimit > 100000 THEN 'VIP'
        WHEN creditLimit > 70000 THEN 'Platinum'
        ELSE 'Bronze'
    END as grade
FROM customers;

SELECT orderNumber, status,
	CASE
		WHEN status = 'In Process' THEN '주문중'
        WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
    END AS 'details'
FROM orders;