-- 문제 1
SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (SELECT avg(MSRP) FROM products)
ORDER BY
	MSRP;

-- 문제 2
SELECT customerNumber, customerName
FROM customers
WHERE customers.customerNumber IN (
	SELECT orders.customerNumber
    FROM orders
    WHERE orderDate >=20030106 AND
    orderDate <= 20030326
    )
ORDER BY
	customerNumber;

-- 문제 3
SELECT productCode, productName, productLine, MSRP
FROM products
WHERE productLine = 'Classic Cars'
ORDER BY MSRP DESC
LIMIT 1
;

-- 문제 4
SELECT customerNumber, customerName, country
FROM customers
WHERE country IN (
		SELECT country
        FROM
		(SELECT country, COUNT(*)
        FROM customers
        GROUP BY country
        ORDER BY COUNT(*) DESC
        LIMIT 1
        ) AS maxCount
        )
ORDER BY
	customerNumber
;
        
-- 문제 5
SELECT customerNumber, customerName, order_count
FROM (
		SELECT customerNumber, COUNT(*) AS 'order_count'
		FROM orders
		GROUP BY customerNumber
		ORDER BY order_count DESC
		LIMIT 1
	) AS maxOrder
LEFT JOIN customers USING (customerNumber)
;

-- 문제 6
SELECT productCode, productName
FROM products
WHERE
	productCode IN (
		SELECT productCode
		FROM orderdetails
		INNER JOIN orders USING (orderNumber)
		WHERE year(orderDate) = 2004
	)
ORDER BY
	productCode DESC
;