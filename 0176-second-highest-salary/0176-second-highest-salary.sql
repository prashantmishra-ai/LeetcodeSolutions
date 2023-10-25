# Write your MySQL query statement below
SELECT (
SELECT DISTINCT salary
From Employee
ORDER BY salary desc
limit 1 offset 1) As SecondHighestSalary;