class Solution(object):
    def Totalsum(self,start,i,num):
        sum=0
        for j in range(start,i+1):
            sum+=num[j]
        return sum

    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum=0
        n=len(nums)
        for i in range(n):
            start=max(0,i-nums[i])
            totalsum+=self.Totalsum(start,i,nums)
        return totalsum




        