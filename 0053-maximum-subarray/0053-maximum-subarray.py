class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        c_sum=0
        for i in nums:
            if c_sum<0:
                c_sum=0
            c_sum+=i
            max_sum=max(max_sum,c_sum)
        return max_sum