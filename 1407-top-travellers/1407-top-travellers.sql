# Write your MySQL query statement below
select a.name, ifnull(sum(distance),0) as travelled_distance from (rides as b  right join users as a on a.id=b.user_id) group by user_id order by sum(distance) desc, a.name asc
