class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_key=set(nums)
        max_count=0
        for i in nums:
            count=1
            if (i-1) not in hash_key:
                j=i+1
                while j in hash_key:
                        count=count+1
                        j=j+1
                if count>max_count:
                    max_count=count
        return max_count
                        
                        
                
            
        