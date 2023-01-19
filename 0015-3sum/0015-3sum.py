class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i!=0:
                if nums[i-1]==nums[i]:
                    continue
            if nums[i]>0:
                break
            l=i+1
            r=len(nums)-1
            while r>l:
                sum=nums[i]+nums[l]+nums[r]
                if sum==0:
                    output.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                elif sum>0:
                    r-=1
                else:
                    l+=1
        return output
    

