class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1=0
        num2=0
        for i in range (1,n+1):
            num1, num2 = (num1, num2 + i) if i % m == 0 else (num1 + i, num2)
              
              
        
        return num1-num2


        