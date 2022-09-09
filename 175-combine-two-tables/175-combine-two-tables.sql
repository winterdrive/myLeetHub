# Write your MySQL query statement below
select a.firstName as firstName, a.lastName as lastName, b.city as city, b.state as state from person a left join address b on a.personID = b.personId