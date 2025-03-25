class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for item in nums:
            freq[item]=freq.get(item,0)+1
        unique_element=[key for key,value in freq.items()if value==1]
        return unique_element[0]
