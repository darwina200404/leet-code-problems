class Solution(object):
    def findFrequency(self,a,t):
        for i in range(len(t)):
            if (t[i]==a):
                return i
        return 0

    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n=len(s)
        freq=[0]*n
        total=0
        for i in range(n):
            freq[i]=self.findFrequency(s[i],t)
            diff=abs(i-freq[i])
            total+=diff
        return total
        

        
        
        