# Write your MySQL query statement below
select Customers.name as Customers FROM Customers where Customers.id not in (select Orders.customerId FROM Orders)