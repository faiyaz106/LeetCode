# https://leetcode.com/problems/detect-capital/description/
# Time complexity: O(n) 
# Space Complexity: O(1)
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<2:
            return True

        if word[0].islower() and word[-1].isupper():
                return False
        left=1
        right=len(word)-1
        while right>=left:
            if (word[left].islower()==word[-1].islower()) and (word[right].islower()==word[-1].islower()):
                right=right-1
                left=left+1
            else:
                return False
        
        return True


            
