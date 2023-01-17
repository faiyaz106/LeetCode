# Write your MySQL query statement below
select ifnull((select distinct e.salary  from
(select *, DENSE_RANK() OVER(order by salary desc) as rn from Employee) as e
where e.rn=2), null) as SecondHighestSalary