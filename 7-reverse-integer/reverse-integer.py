class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        rev=0
        sign=1 if x>0 else -1
        x=abs(x)

        while x!=0:
            digit=x%10
            rev=rev*10+digit
            x//=10
        if rev>2**31-1 or rev<-2**31:
            return 0
        return sign*rev
        
        