class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        
        """
        
        ans=""
        w1=len(word1)
        w2=len(word2)
        i=0
        while(w1>i and w2> i):
            ans+=word1[i]
            ans+=word2[i]
            i+=1
        ans+=word1[i:]
        ans+=word2[i:]
        return ans
        




        