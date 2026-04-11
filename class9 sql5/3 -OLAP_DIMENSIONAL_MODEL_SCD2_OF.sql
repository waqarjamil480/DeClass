use classicmodels_olap;

-- RESETTING THE dim_products for a fresh start
call classicmodels_olap.create_dim_products();

-- WORKING OUT SCD 2 IMPLEMENTATION

drop table if exists classicmodels_olap.products_dim_scd2;
create table classicmodels_olap.products_dim_scd2
as (select productLine, productCode, productName, productScale, 
productVendor, productDescription, quantityInStock, buyPrice, MSRP, 
textDescription, htmlDescription, image
from products_dim
);

show create table products_dim_scd2; -- HERE WE CAN SEE THAT WE DON'T HAVE ANY PRIMARY KEY, WE'RE JUST ADDING THE DATA INTO THIS

select * from products_dim_scd2;

ALTER TABLE `classicmodels_olap`.`products_dim_scd2` 
ADD COLUMN `Product_Dim_Key` INT NOT NULL AUTO_INCREMENT FIRST, -- SURROGRATE KEY FOR PRODUCT DIM
ADD PRIMARY KEY (`Product_Dim_Key`), -- SURROGATE WILL ALSO BE PRIMARY KEY OF THIS PRODUCT DIM SCD2
ADD COLUMN `Effective_From` DATETIME DEFAULT '2000-01-01 00:00:00',
ADD COLUMN `Effective_To` DATETIME DEFAULT '2099-12-31 00:00:00',
ADD COLUMN `is_Latest_Record` TINYINT GENERATED ALWAYS AS (CASE WHEN EFFECTIVE_TO = '2099-12-31' THEN TRUE ELSE FALSE END);

truncate table products_dim_scd2;

insert into classicmodels_olap.products_dim_scd2 
(productLine, productCode, productName, productScale, 
productVendor, productDescription, quantityInStock, buyPrice, MSRP, 
textDescription, htmlDescription, image,effective_from)  
select productLine, productCode, productName, productScale, 
productVendor, productDescription, quantityInStock, buyPrice, MSRP, 
textDescription, htmlDescription, image,updated_at
from products_dim;

SELECT * FROM classicmodels_olap.products_dim_scd2;
select count(*) from classicmodels_olap.products_dim_scd2; -- 110 records

-- TEST CASES 

-- UPDATING A PRODUCT LINE FOR PRODUCT
update products_dim set productLine='Super Cars' , updated_at=now() where productCode='S10_1949' ;

-- UPDATING A PRODUCT LINE FOR PRODUCT TWICE
update products_dim set productLine='Trucks and Buses' , updated_at=now() where productCode='S10_1678' ;
-- select * from products_dim where productCode = 'S10_1678';
update products_dim set productLine='Motorcycles' , updated_at=now() where productCode='S10_1678' ;
-- select * from products_dim where productCode = 'S10_1678';


-- UPDATING A PRODUCT VENDOR FOR PRODUCT IN LAST TEST CASE
update products_dim set productVendor='Exotic Metal Creations' , updated_at=now() where productCode='S10_1678' ;
update products_dim set productVendor='Nuclear Metal Creations' , updated_at=now() where productCode='S10_1678' ;

-- CREATING A NEW PRODUCT
INSERT INTO `classicmodels_olap`.`products_dim`
(`productLine`,`productCode`, `productName`,`productScale`, `productVendor`,`productDescription`,`quantityInStock`, `buyPrice`, `MSRP`, `textDescription`, `htmlDescription`, `image`, `Created_at`, `Updated_at`)
VALUES ('4x4 Daala','ToyotaRevo-007','Revo Black','30:40','Haji Sb Automobiles','Kaala Daala Aya, Dhoom Maachata Aya',10,54231,52541233,NULL,NULL,NULL,now(),NULL);

-- DELETE EXISTING PRODUCT
DELETE FROM `classicmodels_olap`.`products_dim`
WHERE PRODUCTCODE='S10_2016';


-- DML TO CLOSE OLD RECORDS IN PRODUCT_DIM_SCD2 FOR PRODUCTS UPDATED
update products_dim_scd2 pdscd2
left join products_dim pd on pdscd2.productcode=pd.productcode
set pdscd2.effective_to=pd.updated_at
where 
pd.updated_at>pd.created_at -- THOSE RECORDS WHICH WERE UPDATED POST CREATION #CHANGE_DIMENSION
and pdscd2.effective_to='2099-12-31' -- AND THOSE RECORDS WHICH HAVE ACTIVE RECORD IN SCD (SO THAT WE DON'T WASTE COMPUTE TO UPDATE ALREADY CLOSED)
and (pd.ProductLine!=pdscd2.ProductLine or pd.ProductVendor!=pdscd2.ProductVendor) -- THESE ATTRIBUTES WILL BE TRACKED WHEN UPDATING THE SCD AGAINST PRODUCTCODE
;

select * from products_dim_scd2 where productCode = 'S10_1949';
select * from products_dim_scd2 where productCode = 'S10_1678';

-- DML TO OPEN NEW UPDATED RECORDS IN PRODUCT_DIM_SCD < UPDATE IN PREVIOUS STEP
INSERT INTO products_dim_scd2 (productLine, productCode, productName, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP, textDescription, htmlDescription, image, Effective_From, Effective_to)
  (SELECT pd.productLine,
          pd.productCode,
          productName,
          productScale,
          pd.productVendor,
          productDescription,
          quantityInStock,
          buyPrice,
          MSRP,
          textDescription,
          htmlDescription,
          image,
          updated_at Effective_From,
          '2099-12-31 00:00:00' Effective_to
   FROM products_dim pd
   LEFT JOIN
     (SELECT productcode,
             productline,
             ProductVendor,
             effective_to
      FROM products_dim_scd2) pdscd2 ON (pdscd2.productcode=pd.productcode
                                         AND pdscd2.effective_to='2099-12-31'
										/* TO PICK CURRENT ACTIVE RECORDS ONLY TO CHECK CHANGE OF ATTRIBUTES; THIS WILL PREVENT US FOR FETCHING HISTORICAL RECORDS.... ONLY CURRENTLY OPENED RECORDS, It ensures you are only checking against the most recent version of each product in products_dim_scd2 when deciding whether to insert a new version.*/
                                        )
   WHERE (pd.updated_at>pd.created_at -- THOSE RECORDS WHICH WERE UPDATED POST CREATION #CHANGE_DIMENSION

          AND (pdscd2.productcode IS NULL)
          /*
			This comes from a LEFT JOIN, so:
			If a match is found → pdscd2.productcode will have a value
			If NO match is found → pdscd2.productcode will be NULL
            
            the where condition (pd.updated_at > pd.created_at) is the dividing factor, which says that in 
            product_dim_scd2 table, we don't find values where updated_at is greater than created_at for 
            2 products i.e. S10_1678 and S10_1949
            
            AND ULTIMATELY this query says: PICKS RECORDS THAT DO NOT HAVE ANY ACTIVE VERSION IN SCD2
          */
));

select * from products_dim_scd2 where productCode = 'S10_1949';
select * from products_dim_scd2 where productCode = 'S10_1678';

-- DML TO INTRODUCE ONLY NEW RECORDS IN PRODUCT_DIM_SCD
insert into products_dim_scd2  (productLine, productCode, productName, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP, textDescription, htmlDescription, image, Effective_From, Effective_to)
(select pd.productLine, pd.productCode, productName, productScale, pd.productVendor, productDescription, quantityInStock, buyPrice, MSRP, textDescription, htmlDescription, image, Created_at Effective_From, '2099-12-31' Effective_to 
from products_dim pd
where not exists (select * from products_dim_scd2 where products_dim_scd2.productCode=pd.productCode) -- IF PRODUCT DOESNT HAVE A HISTORY IN SCD THEN CREATE THE FIRST RECORD
);

select * from products_dim_scd2 where productCode = 'ToyotaRevo-007';

-- DML TO CLOSE OLD RECORDS IN PRODUCT_DIM_SCD FOR PRODUCTS DELETED
update products_dim_scd2 pdscd2
left join products_dim pd on pdscd2.productcode=pd.productcode
set pdscd2.Effective_To = now()
where 
pd.productCode is null -- THOSE RECORDS WHICH WERE DELETED POST CREATION #DELETE_DIMENSION
and pdscd2.effective_to = '2099-12-31 00:00:00' -- AND THOSE RECORDS WHICH HAVE ACTIVE RECORD IN SCD (SO THAT WE DON'T WASTE COMPUTE TO UPDATE ALREADY CLOSED)
;

select * from products_dim_scd2 where productcode='S10_2016';

select  product_dim_key,productLine, productCode, productName, productVendor, Effective_From, Effective_to,is_latest_record from products_dim_scd2 where productcode in ('S10_1949','S10_1678','ToyotaRevo-007','S10_2016') order by productcode,effective_from,effective_to;

/*delete from products_dim_scd2 where productcode='BOE-737' and productline='Aeroplanes';*/

#drop table products_dim_scd2;

DROP TABLE IF EXISTS classicmodels_olap.order_fact_scd2;

create table classicmodels_olap.order_fact_scd2 as (
	select od.orderNumber
		,year(o.orderDate)*10000+month(o.orderDate)*100+day(o.orderDate) as orderDate -- FORMATTED DATE WILL BE USED TO LINK DATE DIMENSION
	,PDSCD2.Product_Dim_Key,C.customerNumber,E.employeenumber -- OUR DIMENSION REPRESENTATIVES
	,od.quantityOrdered Total_Order_Quantity,od.priceEach*od.quantityOrdered Total_Sale_Amount -- OUR FACT MEMBERS
	from classicmodels.orderdetails OD
	left join classicmodels.orders O using (ordernumber) -- TO CREATE SINGLE FACT
	left join classicmodels_olap.products_dim_scd2 PDSCD2 
		on OD.ProductCode=PDSCD2.ProductCode -- TO LINK ON NATURAL KEYS / BUSINESS KEY AND GET SURROGATE KEY IN RETURN
	and O.orderDate >= PDSCD2.effective_from and O.orderDate < PDSCD2.effective_to -- TO GET THE RIGHT SURROGATE KEY POPULATED AS PER VERSION AT ORDERDATE
	left join classicmodels_olap.customers_dim C using (customernumber) -- TO LINK CUSTOMER DIMENSION
	left join classicmodels_olap.employees_dim E on C.salesrepEmployeeNumber=E.employeenumber -- TO LINK EMPLOYEE DIMENSION (BRIDGED BY CUSTOMER)
);

SELECT * FROM classicmodels_olap.order_fact_scd2;

-- CREATING RELATIONSHIPS FOR DIMENSIONAL MODEL
ALTER TABLE `classicmodels_olap`.`order_fact_scd2` 
MODIFY COLUMN orderDate BIGINT(20), -- TO ALIGN WITH DATE_DIM DATE_ID KEY DATA TYPE
ADD PRIMARY KEY(orderNumber,Product_Dim_Key),
ADD CONSTRAINT `PROD_ID_FK_SCD2` foreign key(Product_Dim_Key) references classicmodels_olap.products_dim_scd2(Product_Dim_Key) ON DELETE NO ACTION,
ADD CONSTRAINT `EMP_ID_FK_SCD2` foreign key(employeeNumber) references classicmodels_olap.employees_dim(employeeNumber),
ADD CONSTRAINT `CUST_ID_FK_SCD2` foreign key(customerNumber) references classicmodels_olap.customers_dim(customerNumber),
ADD CONSTRAINT `ORDERDATE_ID_FK_SCD2` foreign key(orderDate) references classicmodels_olap.date_dim(date_id) ON DELETE NO ACTION
;

call extend_dim_date(DATE_FORMAT(now(), '%Y-%m-01'),LAST_DAY(now()));

SELECT count(*) FROM classicmodels_olap.order_fact_scd2;

select * from classicmodels.orderdetails where productcode='S10_1949';

select * from classicmodels.orders where orderNumber=10103;

/* run below commands if inserted earlier while testing code
delete from classicmodels.orders where orderNumber = '20000';
delete from classicmodels.orderdetails where orderNumber = '20000';
*/

INSERT INTO classicmodels.orders (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)
VALUES ('20000', now(), '2003-02-07', '2003-02-02', 'Shipped', NULL, '121');

-- due to trigger in orderdetails, the below code snippet wasn't running, for the time being we've removed the trigger 
DROP TRIGGER IF EXISTS classicmodels.AfterOrderInsert;

INSERT INTO classicmodels.orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (20000, 'S10_1949' , 26 , 214.52 , 11);

select * from classicmodels.orders;
select * from classicmodels.orderdetails where orderNumber = '20000';
-- DROP THE ABOVE order_fact_scd2 TABLE AND SEE NOW AFTER INSERTING NEW VALUES IN ORDERHEADER & ORDERDETAIL TABLES,
-- A ROW COUNT HAS BEEN INCREASED. AND IT IS CAPTURING CLASSIC AND SUPER CARS ON SEPARATE ROWS.

SELECT * FROM classicmodels_olap.order_fact_scd2 where orderNumber = '20000';

select p.Product_Dim_Key,p.productLine,count(distinct orderNumber) OrderCount,
sum(Total_Sale_Amount) as TotalSales
from classicmodels_olap.order_fact_scd2
right join products_dim_scd2 p using (product_dim_key)
where p.productCode='S10_1949'
group by p.productLine, p.Product_Dim_Key;

select min(date), max(date) from date_dim;
SELECT @@FOREIGN_KEY_CHECKS;
select * from date_dim;



/* CREATED A DUMMY TABLE TO SHOW THE ERROR THAT BECAUSE DATE_DIM DOESN'T
HAVE VALUES FOR YEAR 2050, IT GIVES US THE ERROR BECAUSE OF FOREIGN
CONSTRAINT */

CREATE TABLE Persons_Dummy (
    PersonID int,
    PersonName varchar(255),
    CreatedAt bigint,
    FOREIGN KEY (CreatedAt) REFERENCES date_dim(date_id)  
);

insert into Persons_Dummy (PersonID, PersonName, CreatedAt)
VALUES (100,'Umair Hanif',20500101)