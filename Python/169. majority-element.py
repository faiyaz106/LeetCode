# https://leetcode.com/problems/majority-element/description/

# Solution 1. Time Complexity: O(n) and Space Complexity: O(1)

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

# Solution 2. Time Complexity: O(n) and Space Complexity: O(n)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        major_count=0
        major_element=nums[0]
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
                if hashmap[i]>major_count:
                    major_count=hashmap[i]
                    major_element=i
                else:
                    continue
            else:
                hashmap[i]=1

        return major_element
