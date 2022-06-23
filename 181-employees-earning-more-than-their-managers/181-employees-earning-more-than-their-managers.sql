/* Write your PL/SQL query statement below */
select name as Employee from Employee emp
where
    exists (select 1 from Employee mgr 
           where emp.managerId = mgr.id and mgr.salary < emp.salary);