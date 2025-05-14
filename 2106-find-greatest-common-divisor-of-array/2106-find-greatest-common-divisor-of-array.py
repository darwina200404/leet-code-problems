class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small=min(nums)
        large=max(nums)
        max_gcd=1
        for i in range(2,small+1):
            if (large % i==0 and small%i==0):
                max_gcd=max(1,i)
                
        return max_gcd