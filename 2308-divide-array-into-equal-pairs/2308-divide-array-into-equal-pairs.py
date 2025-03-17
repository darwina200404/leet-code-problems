class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq_dic={}
        for num in nums:
            freq_dic[num]=freq_dic.get(num,0)+1
        for num,count in freq_dic.items():
            if count % 2 !=0:
                return False
        return True

        