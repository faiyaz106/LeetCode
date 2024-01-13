class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s.split())
        reverse=s.pop()
        while len(s)>0:
            reverse+=" "+s.pop()
        return reverse