# https://leetcode.com/problems/climbing-stairs/description/
# Time complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first=1
        second=1
        for i in range(n-1):
            temp=first
            first=temp+second
            second=temp
        
        return first

