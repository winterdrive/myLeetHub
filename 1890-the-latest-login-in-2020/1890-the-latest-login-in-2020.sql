# Write your MySQL query statement below
select user_id,max(time_stamp) as last_stamp  from logins where 
time_stamp in
(select time_stamp from logins where time_stamp between '2020-01-01 00:00:00.000' and '2021-01-01 00:00:00.000' order by time_stamp desc)
and 
time_stamp not in
(select time_stamp from logins where time_stamp not between '2020-01-01 00:00:00.000' and '2021-01-01 00:00:00.000' order by time_stamp desc) 
group by user_id