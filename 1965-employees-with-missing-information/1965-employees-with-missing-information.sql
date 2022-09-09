# Write your MySQL query statement below

select * from (
select salaries.employee_id from employees right join salaries on employees.employee_id=salaries.employee_id where employees.name is null 
union
select employees.employee_id from employees left join salaries on employees.employee_id=salaries.employee_id where salaries.salary is null ) result
order by employee_id asc