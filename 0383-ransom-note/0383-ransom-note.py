class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict_m={}
        for i in magazine:
            if i in dict_m:
                dict_m[i]+=1
            else:
                dict_m[i]=1
        for i in ransomNote:
            if i in dict_m and dict_m[i]>0:
                dict_m[i]-=1
            else:
                return False
        return True