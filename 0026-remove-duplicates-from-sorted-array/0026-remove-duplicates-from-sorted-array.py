class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l=0
        r=1
        count=1
        for i in range(0,n-1):
            if nums[i]==nums[i+1]:
                continue
            else:
                nums[count]=nums[i+1]
                count+=1
                
        return count
            