# Write your MySQL query statement below
select d.name as Department, sq.name as Employee, sq.salary as Salary
from 
(select *, dense_rank() over(partition by departmentId order by salary desc) as rn 
from Employee) as sq join Department as d on sq.departmentId =d.id 
where sq.rn<=3