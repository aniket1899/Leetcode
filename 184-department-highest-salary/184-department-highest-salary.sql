# Write your MySQL query statement below

select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e, Department d
where e.departmentId = d.id
and e.salary >= ALL(select salary from Employee e2 where e2.departmentId = e.departmentId);