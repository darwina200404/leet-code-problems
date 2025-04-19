class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        for pivot in range (n+1):
            beforeSum=(pivot)*(1+pivot)/2
            AfterSum=(n-pivot+1)*(pivot+n)/2
            if beforeSum==AfterSum:
                return pivot
        return -1
        
        