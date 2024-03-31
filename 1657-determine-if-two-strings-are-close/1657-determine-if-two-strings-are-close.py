class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Corner cases 
        if len(word1)!=len(word2):
            return False 
        w1_count={}
        w2_count={}
        for i,j in zip(word1,word2): 
            if i in w1_count:
                w1_count[i]+=1 
            else: 
                w1_count[i]=1
            if j in w2_count: 
                w2_count[j]+=1
            else: 
                w2_count[j]=1 
        if w1_count.keys()!=w2_count.keys():
            return False
        w1=list(w1_count.values())
        w2=list(w2_count.values())
        if sorted(w1)==sorted(w2): 
            return True
        return False