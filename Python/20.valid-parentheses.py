# https://leetcode.com/problems/valid-parentheses/
# Time Complexity:O(n)
# Space Complexity:O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if  i in dict.keys():
                if stack and dict[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if len(stack)==0:
            return True
        else:
            return False





            


                
