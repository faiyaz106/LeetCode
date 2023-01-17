# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1

        left=1
        right=n
        mid=int((left+right)//2)
        while (right-left)>0:
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1
            if not isBadVersion(mid):
                left=mid
                mid=int((mid+right)//2)
            else:
                right=mid
                mid=int((mid+left)//2)
            
        
    