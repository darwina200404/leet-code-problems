class Solution(object):
    
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        while(original in nums):
            original=2*original
        return original


        