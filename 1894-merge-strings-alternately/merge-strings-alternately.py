class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        
        """
        
        ans=""
        i=0
        while(len(word1)>i and len(word2)> i):
            ans+=word1[i]
            ans+=word2[i]
            i+=1
        ans+=word1[i:]
        ans+=word2[i:]
        return ans
        




        