class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        nums.sort()
        n=len(nums)-1
        left=0
        right=n
        while left<right:
            if ((nums[left]+nums[right])<target):
                count+=right-left
                left+=1
            else:
                right-=1
        return count

