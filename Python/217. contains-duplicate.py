# https://leetcode.com/problems/contains-duplicate/description/
# Time Complexity: O(n) and Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_=set()
        for i in range(len(nums)):
            if nums[i] in set_:
                return True
            else:
                set_.add(nums[i])

        return False
