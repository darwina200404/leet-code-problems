class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evenCount=0
        n=len(nums)
        ans=[0]*n
        for num in nums:
            if(num%2==0):
                evenCount+=1
        for i in range(evenCount,n):
            ans[i]=1
        return ans
        