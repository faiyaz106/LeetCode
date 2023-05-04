class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        n=0
        l=[]
        while 10**n<=x:
            l.append((x//10**n)%10)
            n+=1
        for i in range(0,(len(l)//2)):
            if l[i]==l[len(l)-1-i]:
                continue
            else:
                return False
        return True
            
            
            
        