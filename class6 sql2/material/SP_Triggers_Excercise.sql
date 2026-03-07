use classicmodels;

SET SQL_SAFE_UPDATES = 0; -- TO AVOID Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.

-- CREATING AN AUTO SUMAMRY AT ORDER LEVEL BY USING TRIGGER

DROP PROCEDURE IF EXISTS CalculateTotalOrderVal;

DELIMITER //
CREATE PROCEDURE CalculateTotalOrderVal(
	IN pOrderNumber INT,
    IN DateInserted DATE
)
BEGIN
	insert into order_value
	select pOrderNumber, sum(priceeach*quantityordered) total_amount, DateInserted
    from orderdetails 
    WHERE orderNumber = pOrderNumber
    group by orderNumber;
END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS AfterOrderInsert;

DELIMITER //
CREATE TRIGGER AfterOrderInsert
AFTER INSERT ON orderdetails
FOR EACH ROW
BEGIN
	CALL CalculateTotalOrderVal(NEW.orderNumber,now());
END;
//
DELIMITER ;

drop table order_value;

create table order_value as (select orderNumber, sum(priceeach*quantityordered) total_amount, now() insert_date from orderdetails group by orderNumber);

select * from order_value where ordernumber=20405;

INSERT INTO `classicmodels`.`orders`
(`orderNumber`,
`orderDate`,
`requiredDate`,
`shippedDate`,
`status`,
`comments`,
`customerNumber`)
VALUES
(20405,
'2023-09-02',
'2023-09-02',
'2023-09-02',
'Shipped',
'FAKE ORDER',
363);

INSERT INTO `classicmodels`.`orderdetails`
(`orderNumber`,
`productCode`,
`quantityOrdered`,
`priceEach`,
`orderLineNumber`)
VALUES
(20405,
'S18_1749',
5,
1000,
4);

delete from orders where orderNumber=20405;
delete from orderdetails where orderNumber=20405;

-- CLASS EXERCISE
-- 1. NOW YOUR TURN TO MAKE A PROCEDURE THAT DELETE order_value IF USER DELETES THE Order from orderDetails and Order Table as well
-- 2. NOW YOUR TURN TO MAKE A PROCEDURE THAT UPDATES order_value IF USER UPDATES THE quantityOrdered or priceEach AGAINST EXISTING ORDERS