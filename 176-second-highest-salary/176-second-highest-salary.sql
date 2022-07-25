/* Write your PL/SQL query statement below */

SELECT max(e1.salary) as SecondHighestSalary  from Employee e1
                        WHERE e1.salary <> (SELECT max(salary) FROM Employee);