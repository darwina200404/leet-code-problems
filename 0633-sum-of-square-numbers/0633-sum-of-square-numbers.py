class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left=0
        right=int(math.sqrt(c))
        while left<=right:
            n=left*left+right*right
            if(n==c):
                return True
            elif (n<c):
                left+=1
            else:
                right-=1
        return False
        