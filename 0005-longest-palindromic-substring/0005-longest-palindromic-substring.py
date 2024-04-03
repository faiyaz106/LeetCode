class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        max_str=s[0]
        for i in range(0,n-1):
            # odd case 
            left=i-1
            right=i+1 
            temp_str=s[i]
            while left>=0 and right<n: 
                if s[left]==s[right]:
                    temp_str=s[left]+temp_str+s[right]
                    right=right+1
                    left=left-1
                else: 
                    break 
            if len(temp_str)>len(max_str):
                max_str=temp_str          
            # even case 
            # at first check ajacent character is same 
            if s[i]==s[i+1]:
                left=i-1
                right=i+2 
                temp_str=s[i]+s[i+1]
                while left>=0 and right<n: 
                    if s[left]==s[right]:
                        temp_str=s[left]+temp_str+s[right]
                        right=right+1
                        left=left-1
                    else: 
                        break 
                if len(temp_str)>len(max_str):
                    max_str=temp_str  
        return max_str
            
            