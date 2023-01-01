#https://leetcode.com/problems/word-pattern/discussion/
#Time Complexity: O(n) Here n=len(pattern)
#Space Complexity: O(m) Here m=len(pattern)+len(s.split())


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if len(pattern)!=len(s.split()):
            return False

        dict_1={}
        dict_2={}
        for i in range(len(pattern)):
            if pattern[i] in dict_1 and dict_1[pattern[i]]!=(s.split())[i]:
                return False
            if  (s.split())[i] in dict_2 and pattern[i] not in dict_1:
                return False
            if pattern[i] not in dict_1 and (s.split())[i] not in dict_2:
                dict_1[pattern[i]]=(s.split())[i]
                dict_2[(s.split())[i]]=None

        return True
