# Write your MySQL query statement below

select distinct product_id,product_name
from
Product natural join Sales
group by product_id,product_name
having  min(sale_date)>='2019-01-01' and max(sale_date)<='2019-03-31'