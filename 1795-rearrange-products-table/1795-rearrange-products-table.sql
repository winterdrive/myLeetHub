# Write your MySQL query statement below
select a.product_id , 'store1' as store, a.store1 as price from products as a where store1 is not null
union 
select b.product_id , 'store2' as store, b.store2 as price from products as b where store2 is not null
union 
select c.product_id , 'store3' as store, c.store3 as price from products as c where store3 is not null