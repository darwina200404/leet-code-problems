class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            sum=0
            for j in range (i):
                sum=nums[i]+nums[j]
                if(sum<target):
                    count+=1
        return count

        