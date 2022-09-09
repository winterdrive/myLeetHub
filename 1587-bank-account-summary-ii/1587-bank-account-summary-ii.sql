# Write your MySQL query statement below
select a.name , b.balance from users as a join (
select account, sum(amount) as balance from transactions group by account having sum(amount)>10000 ) as b on a.account=b.account