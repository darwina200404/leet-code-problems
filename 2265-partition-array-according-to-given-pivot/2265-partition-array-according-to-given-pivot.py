class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lis1 = [element for element in nums if element < pivot]
        lis2 = [element for element in nums if element == pivot]
        lis3 = [element for element in nums if element > pivot]
        return lis1+lis2+lis3
        

        