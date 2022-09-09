# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
Delete FROM Person where id not in 
(select * from 
 (select min(id) 
  from Person group by Person.email)as t)
# min(id)會是第一次出現的
