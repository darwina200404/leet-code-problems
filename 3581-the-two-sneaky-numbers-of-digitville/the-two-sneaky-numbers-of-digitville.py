class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                a.append(nums[i])
        return a
                


        