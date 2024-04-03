class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_sub=0
        for i in range(0,n):
            sub_str=s[i]
            temp=set()
            temp.add(s[i])
            for j in range(i+1,n):
                if s[j] not in temp: 
                    sub_str+=s[j]
                    temp.add(s[j])
                else:
                    break
            if len(sub_str) > max_sub: 
                max_sub=len(sub_str)
        return max_sub
                
        