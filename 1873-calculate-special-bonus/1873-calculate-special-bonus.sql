# Write your MySQL query statement below
select employee_id , 
case when 
substring(name,1,1)!='M' && employee_id%2!=0 
then salary else 0 end as bonus from employees order by employee_id