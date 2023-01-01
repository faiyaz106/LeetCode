# https://leetcode.com/problems/combine-two-tables/solutions/

# Write your MySQL query statement below

select firstName, lastName,city,state 
from Person left outer join Address on Person.personId=Address.personID;
