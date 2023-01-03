# https://leetcode.com/problems/delete-columns-to-make-sorted/description/
# Time Complexity: O(n*m)  Here n=length of list and m=length of each string
# Space Complexity: O(1) 

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count=0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i]>strs[j+1][i]:
                    count=count+1
                    break

        return count
                

                



                

