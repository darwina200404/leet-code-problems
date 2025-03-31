class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        Sum=sum(nums)
        whole_sum=(n*(n+1))//2
        return whole_sum-Sum
        