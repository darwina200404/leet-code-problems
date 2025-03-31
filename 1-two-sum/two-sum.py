class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table={}
        for index ,val in enumerate(nums):
            diff=target-val
            if diff in table:
                return [index,table[diff]]
            else:
                table[val]=index


        