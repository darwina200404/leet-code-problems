class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        lis=[0]*n
        for i in range(n):
            lis[i]=start+2*i
        return reduce(xor,lis)
        