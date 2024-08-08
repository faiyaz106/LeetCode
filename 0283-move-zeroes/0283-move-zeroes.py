class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        left=0
        right=1
        # Initialize Left and right
        while right<len(nums) and left<right:
            if nums[left]==0 and nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1
                continue
            if nums[left]!=0 and nums[right]!=0:
                left+=1
                right+=1
                continue
            if nums[left]!=0:
                left+=1
            if nums[right]==0:
                right+=1
  
            

        return nums
    
    