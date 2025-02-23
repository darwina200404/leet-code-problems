class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_1 = count_2 = 0
        
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                count_1 += 1
            elif remainder == 2:
                count_2 += 1
        
        return count_1 + count_2
      
        