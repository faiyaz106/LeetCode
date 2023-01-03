# https://leetcode.com/problems/longest-palindrome/
# Time complexity: O(n) and Space Complexity: O(n)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        count=0
        odd=0
        for i in dict.keys():
            if dict[i]%2==0:
                count=count+dict[i]
            else:
                odd=1
                count+=(dict[i]-1)
            
        
        return count+odd
