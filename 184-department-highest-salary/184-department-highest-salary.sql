# Write your MySQL query statement below

select d1.name as Department, e1.name as Employee, e1.Salary as Salary from employee e1, department d1 ,(select departmentId, max(salary) as salary from employee group by departmentId) result

where d1.id=e1.departmentID
and e1.salary = result.salary
and e1.departmentId =result.departmentId
