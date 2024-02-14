class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars)==1:
            return len(chars)
    
        n=len(chars)
        key=chars[-1]
        count=0
        while n>0:
            pop_char=chars.pop()
            n=n-1
            if key==pop_char:
                count=count+1
            else: 
                if count>1 and count<10: 
                    chars.insert(0,str(count))
                if count>9: 
                    temp=str(count)
                    for i in range(0,len(temp)):
                        idx=len(temp)-1-i
                        chars.insert(0,temp[idx])
                chars.insert(0,key)
                key=pop_char
                count=1
        if count>1 and count<10: 
            chars.insert(0,str(count))
        if count>9: 
            temp=str(count)
            for i in range(0,len(temp)):
                idx=len(temp)-1-i
                chars.insert(0,temp[idx])
        chars.insert(0,key)
        return len(chars)
                
                
            
            
            