class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        if len(s)==1 and len(t)==1:
            if s==t:
                return True
            else:
                return False 
        left=0
        right=len(s)-1
        n=len(t)
        for i in range(0,(n-1)/2 + 1):
            if i!=n-i-1:
                if s[left]==t[i]:
                    left=left+1
                if s[right]==t[n-i-1]:
                    right=right-1
            else:
                if s[left]==t[i]:
                    left=left+1
                
            if left>right:
                return True
        
        
        return False
            
            