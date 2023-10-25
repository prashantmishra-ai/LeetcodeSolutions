# Write your MySQL query statement below
SELECT P.firstName, P.lastName, A.city, A.state from Person P
LEFT Join Address A
On P.personId=A.personId
