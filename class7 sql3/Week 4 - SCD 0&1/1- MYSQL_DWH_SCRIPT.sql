DELIMITER //

DROP PROCEDURE IF EXISTS classicmodels.setup_datawarehouse //
CREATE PROCEDURE classicmodels.setup_datawarehouse()
BEGIN
	DROP DATABASE IF EXISTS classicmodels_olap;
	CREATE DATABASE classicmodels_olap;
    
END //

delimiter ;

call classicmodels.setup_datawarehouse();

DELIMITER //

DROP PROCEDURE IF EXISTS classicmodels_olap.create_dim_employees //
CREATE PROCEDURE classicmodels_olap.create_dim_employees()
BEGIN
	drop table if exists classicmodels_olap.employees_dim;
	create table classicmodels_olap.employees_dim as (
		select * from classicmodels.employees
		left join classicmodels.offices using (officecode)
    );
	
    ALTER TABLE classicmodels_olap.employees_dim
    
    -- DECLARING PRIMARY KEY
	ADD PRIMARY KEY(employeeNumber),
	
    -- FOR CHANGE DATA CAPTURE LATER
    ADD COLUMN `Created_at` DATETIME NULL DEFAULT '2000-01-01 00:00:00',
	ADD COLUMN `Updated_at` DATETIME NULL DEFAULT '2000-01-01 00:00:00';
    
END //

DROP PROCEDURE IF EXISTS classicmodels_olap.create_dim_customers //
CREATE PROCEDURE classicmodels_olap.create_dim_customers()
BEGIN
	drop table if exists classicmodels_olap.customers_dim;
	create table classicmodels_olap.customers_dim as (
		select * from classicmodels.customers
    );
    
    ALTER TABLE classicmodels_olap.customers_dim
	
    -- DECLARING PRIMARY KEY
	ADD PRIMARY KEY(customerNumber),
    
    -- FOR CHANGE DATA CAPTURE LATER
    ADD COLUMN `Created_at` DATETIME NULL DEFAULT '2000-01-01 00:00:00',
	ADD COLUMN `Updated_at` DATETIME NULL DEFAULT '2000-01-01 00:00:00';
    
END //

DROP PROCEDURE IF EXISTS classicmodels_olap.create_dim_products //
CREATE PROCEDURE classicmodels_olap.create_dim_products()
BEGIN
	drop table if exists classicmodels_olap.products_dim;
	create table classicmodels_olap.products_dim as (
		select * from classicmodels.products
		left join classicmodels.productlines using (productline)
    );
    
    ALTER TABLE `classicmodels_olap`.`products_dim` 
    
    -- DECLARING PRIMARY KEY
	ADD PRIMARY KEY(productCode),
	
    -- FOR CHANGE DATA CAPTURE LATER
    ADD COLUMN `Created_at` DATETIME NULL DEFAULT '2000-01-01 00:00:00',
	ADD COLUMN `Updated_at` DATETIME NULL DEFAULT '2000-01-01 00:00:00';

END //

DELIMITER ;


call classicmodels_olap.create_dim_employees();
call classicmodels_olap.create_dim_customers();
call classicmodels_olap.create_dim_products();
call classicmodels_olap.create_dim_date('2002-01-01','2006-12-31');

#delete from classicmodels.orderdetails where orderNumber=20000;
#delete from classicmodels.orders where orderNumber=20000;


select min(date),max(date) from classicmodels_olap.date_dim;

select * from classicmodels_olap.customers_dim;