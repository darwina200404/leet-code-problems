class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(nums)
        ans[0]=nums[0]
        for i in range(1,len(nums)):
            ans[i]+=nums[i]+ans[i-1]
        return ans



        