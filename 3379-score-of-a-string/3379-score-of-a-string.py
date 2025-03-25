class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        for i in  range(len(s)-1):
            differnce=abs(ord(s[i])-ord(s[i+1]))
            sum+=differnce

        return sum
        