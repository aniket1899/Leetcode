/* Write your PL/SQL query statement below */

select c.name as Customers from (select id as ID from Customers
minus
select customerID as ID from Orders) q, Customers c
where c.ID = q.ID;