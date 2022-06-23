/* Write your PL/SQL query statement below */
-- select name as Employee from Employee emp
-- where
--     exists (select 1 from Employee mgr 
--            where emp.managerId = mgr.id and mgr.salary < emp.salary);

select e.name as Employee from Employee e inner join Employee m on e.managerId = m.id and e.salary > m.salary;