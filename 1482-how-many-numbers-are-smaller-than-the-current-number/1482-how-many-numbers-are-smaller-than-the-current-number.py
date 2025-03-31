class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums=sorted(nums)
        ans=[]
        table={}
        for i,num in enumerate (new_nums):
            if num not in table:
                table[num]=i
        for i in nums:
            ans.append(table[i])
        return ans

        