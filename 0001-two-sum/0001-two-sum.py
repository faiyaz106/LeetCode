class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        n=len(nums)
        for i in range(n):
            residue=target-nums[i]
            if (residue in dict ):
                return [i,dict[residue]]
            else:
                dict[nums[i]]=i