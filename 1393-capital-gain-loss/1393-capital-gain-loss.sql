# Write your MySQL query statement below
select stock_name, sum(price) as capital_gain_loss from 
((select stock_name, price as price from stocks where operation='sell')
union All 
(select stock_name, -price as price from stocks where operation='buy')) result group by stock_name
