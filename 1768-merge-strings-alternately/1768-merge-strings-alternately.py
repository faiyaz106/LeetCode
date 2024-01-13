class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        signal=True
        output=""
        for i,j in zip(word1,word2):
            output+=i+j
        if len(word1)==len(word2):
            return output
        elif len(word1)>len(word2):
            output+=word1[len(word2):]
        else:
            output+=word2[len(word1):]
        return output