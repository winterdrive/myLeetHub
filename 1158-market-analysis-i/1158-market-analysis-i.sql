# Write your MySQL query statement below
select 
u1.user_id as buyer_id, 
u1.join_date as join_date, 
count(o1.order_id) as orders_in_2019 
from 
Users u1 
left join 
(select * from orders where year(order_date)=2019 ) o1
on 
u1.user_id=o1.buyer_id
group by 
u1.user_id

