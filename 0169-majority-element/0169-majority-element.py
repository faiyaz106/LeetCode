class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in nums:
            if count==0:
                major_element=i
            if major_element==i:
                count+=1
            else:
                count-=1

        return major_element
