class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0]==target:
            return 0
        if nums[len(nums)-1]==target:
            return len(nums)-1
        if len(nums)==1:
            if nums[0]==target:
                return 0 
            else:
                return -1
        left=0
        right=len(nums)-1
        ptr=(len(nums)-1)//2
        prev=0
        while abs(left-right)!=1:
            if nums[ptr]==target:
                return ptr 
            if target>nums[ptr]:
                left=ptr
                ptr=(ptr+right)//2
            if target<nums[ptr]:
                right=ptr
                ptr=(ptr+left)//2


        return -1
