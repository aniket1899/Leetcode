/* Write your PL/SQL query statement below */

SELECT max(q.salary) as SecondHighestSalary from (SELECT salary from Employee e1
                        WHERE e1.salary <> (SELECT max(salary) FROM Employee)) q;