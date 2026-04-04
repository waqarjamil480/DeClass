use classicmodels_olap;

-- SET foreign_key_checks = 0;

-- ALTER TABLE `classicmodels_olap`.`order_fact` DROP FOREIGN KEY `PROD_ID_FK`;

ALTER TABLE `classicmodels`.`orders` 
CHANGE COLUMN `orderDate` `orderDate` DATETIME NOT NULL ;

-- call classicmodels_olap.create_dim_products();

ALTER TABLE `classicmodels_olap`.`products_dim` 

-- MAKING THEM NULLABLE FOR TESTING PURPOSE
CHANGE COLUMN `productLine` `productLine` VARCHAR(50) NULL ,
CHANGE COLUMN `productName` `productName` VARCHAR(70) NULL ,
CHANGE COLUMN `productScale` `productScale` VARCHAR(10) NULL ,
CHANGE COLUMN `productVendor` `productVendor` VARCHAR(50) NULL ,
CHANGE COLUMN `productDescription` `productDescription` TEXT NULL ,
CHANGE COLUMN `quantityInStock` `quantityInStock` SMALLINT(6) NULL ,
CHANGE COLUMN `buyPrice` `buyPrice` DECIMAL(10,2) NULL ,
CHANGE COLUMN `MSRP` `MSRP` DECIMAL(10,2) NULL ;

-- WORKING OUT SCD 1 IMPLEMENTATION

select * from products_dim;

drop table if exists products_dim_scd1;
create table products_dim_scd1 like products_dim;

insert into products_dim_scd1
select * from products_dim;

select * from products_dim_scd1;
/*
ALTER TABLE `classicmodels_olap`.`products_dim_scd1` 
ADD PRIMARY KEY (`productCode`); -- BECAUSE OF SCD1 THERE IS NO SURROGATE KEY
*/
select * from products_dim_scd1 where productCode = 'S10_1949';

select * from products_dim where productCode = 'S10_1949';

update products_dim set productLine='Super Cars' , updated_at=now() where productCode='S10_1949' ;

select * from products_dim where productCode = 'S10_1949';

update products_dim_scd1 pdscd1
left join products_dim pd on pdscd1.productcode=pd.productcode
set pdscd1.updated_at=pd.updated_at, pdscd1.productLine=pd.productLine , pdscd1.productVendor=pd.productVendor
where 
pd.updated_at > pd.created_at -- THOSE RECORDS WHICH WERE UPDATED POST CREATION #CHANGE_DIMENSION
and (pd.ProductLine!=pdscd1.ProductLine or pd.ProductVendor!=pdscd1.ProductVendor);
/* THIS MEANS THAT WE NEED TO MAKE SURE THAT Super Cars SHOULD NOT BE EQUAL TO Classic Cars, BOTH TABLES SHOULD HAVE DIFFERENT VALUES, 
MEANS THEY AREN'T EQUAL. THIS ALSO SHOWS THAT WE ARE UPDATING ONLY THAT RECORD WHICH WE NEED TO I.E. SHORTLISTING A RECORD ON A MUCH GRANULAR LEVEL
THESE ATTRIBUTES WILL BE TRACKED WHEN UPDATING THE SCD AGAINST PRODUCTCODE */
;

-- FOR ABOVE UPDATE WE CAN CREATE A PROCEDURE AND CALL IT INSIDE A AFTER UPDATE TRIGGER IN MYSQL

DELIMITER //

DROP PROCEDURE IF EXISTS classicmodels_olap.create_fact_orders //
CREATE PROCEDURE classicmodels_olap.create_fact_orders()
BEGIN
	DROP TABLE IF EXISTS classicmodels_olap.order_fact_scd1;
    
	create table classicmodels_olap.order_fact_scd1 as (
		select od.orderNumber
			,year(o.orderDate)*10000+month(o.orderDate)*100+day(o.orderDate) as orderDate -- FORMATTED DATE WILL BE USED TO LINK DATE DIMENSION
		,P.productCode,C.customerNumber,E.employeenumber -- OUR DIMENSION REPRESENTATIVES
        ,od.quantityOrdered Total_Order_Quantity,od.priceEach*od.quantityOrdered Total_Sale_Amount -- OUR FACT MEMBERS
        from classicmodels.orderdetails OD
		left join classicmodels.orders O using (ordernumber) -- TO CREATE SINGLE FACT
		left join classicmodels_olap.products_dim_scd1 P using (productCode) -- TO LINK PRODUCT DIMENSION
		left join classicmodels_olap.customers_dim C using (customernumber) -- TO LINK CUSTOMER DIMENSION
		left join classicmodels_olap.employees_dim E on C.salesrepEmployeeNumber=E.employeenumber -- TO LINK EMPLOYEE DIMENSION (BRIDGED BY CUSTOMER)
    );
    
	-- CREATING RELATIONSHIPS FOR DIMENSIONAL MODEL
    ALTER TABLE `classicmodels_olap`.`order_fact_scd1` 
	
    MODIFY COLUMN orderDate BIGINT(20), -- TO ALIGN WITH DATE_DIM DATE_ID KEY DATA TYPE

    ADD PRIMARY KEY(orderNumber,productCode),
    ADD CONSTRAINT `EMP_ID_FK_SCD1` foreign key(`employeeNumber`) references classicmodels_olap.employees_dim(employeeNumber),
    ADD CONSTRAINT `CUST_ID_FK_SCD1` foreign key(`customerNumber`) references classicmodels_olap.customers_dim(customerNumber),
    ADD CONSTRAINT `PROD_ID_FK_SCD1` foreign key(`productCode`) references classicmodels_olap.products_dim_scd1(productCode) ON DELETE NO ACTION,
    ADD CONSTRAINT `ORDERDATE_ID_FK_SCD1` foreign key(`orderDate`) references classicmodels_olap.date_dim(date_id) ON DELETE NO ACTION
    ;
    
END //

DELIMITER ;

call classicmodels_olap.create_fact_orders();

select * from order_fact_scd1
left join products_dim_scd1 using (productCode)
 where productCode = 'S10_1949';

