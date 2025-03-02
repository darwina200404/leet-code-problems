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
        while(w1>0 and w2> 0):
            ans+=word1[i]
            w1-=1
            ans+=word2[i]
            w2-=1
            i+=1
        ans+=word1[i:]
        ans+=word2[i:]
        return ans
        




        