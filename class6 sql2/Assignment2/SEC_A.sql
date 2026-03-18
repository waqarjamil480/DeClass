-- Q1
SELECT p.productLine, COUNT(DISTINCT o.orderNumber) AS total_orders FROM orders o
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode
GROUP BY p.productLine
HAVING COUNT(DISTINCT o.orderNumber) > 100;


-- Q2
SELECT  CONCAT(m.firstName, ' ', m.lastName) AS manager_name, COUNT(e.employeeNumber) AS employee_count FROM employees e
JOIN employees m  ON e.reportsTo = m.employeeNumber
GROUP BY m.employeeNumber;


-- Q3
SELECT  c.city,
    COUNT(CASE WHEN o.status = 'Shipped' THEN 1 END) AS shipped,
    COUNT(CASE WHEN o.status = 'Cancelled' THEN 1 END) AS cancelled,
    COUNT(CASE WHEN o.status = 'Resolved' THEN 1 END) AS resolved,
    COUNT(CASE WHEN o.status = 'Disputed' THEN 1 END) AS disputed,
    COUNT(CASE WHEN o.status = 'On Hold' THEN 1 END) AS on_hold
FROM customers c  JOIN orders o ON c.customerNumber = o.customerNumber
GROUP BY c.city;


-- Q4
SELECT  o.officeCode, o.city, COUNT(DISTINCT ord.orderNumber) AS total_orders FROM offices o
JOIN employees e ON o.officeCode = e.officeCode
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders ord ON c.customerNumber = ord.customerNumber
GROUP BY o.officeCode, o.city;



-- Q5
SELECT  e.employeeNumber, CONCAT(e.firstName, ' ', e.lastName) AS employee_name, COUNT(ord.orderNumber) AS total_orders
FROM employees e
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders ord ON c.customerNumber = ord.customerNumber
WHERE e.officeCode NOT IN (SELECT officeCode FROM offices WHERE country = 'USA')
GROUP BY e.employeeNumber;



-- Q6
WITH product_sales AS (SELECT p.productLine, p.productName, SUM(od.quantityOrdered) AS total_sold FROM orderdetails od
    JOIN products p ON od.productCode = p.productCode
    GROUP BY p.productLine, p.productName
),
ranked_products AS (SELECT *, DENSE_RANK() OVER (
		PARTITION BY productLine 
		ORDER BY total_sold DESC
	) AS rnk
    FROM product_sales)
SELECT productLine, productName, total_sold
FROM ranked_products
WHERE rnk = 2;
