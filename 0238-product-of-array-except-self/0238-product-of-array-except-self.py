class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=1
        post=1
        out=[1]*len(nums)
        for i in range(0,len(nums)):
            pre*=nums[i]
            if (i+1)<len(nums):
                out[i+1]*=pre
            j=len(nums)-1-i
            if (j-1)>=0:
                post*=nums[j]
                out[j-1]*=post
        return out
            
            