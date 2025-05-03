class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums=sorted(nums)
        ans=[]
        table={}
        for index,val in enumerate(new_nums):
            if val not in table:
                table[val]=index
        for i in nums:
            ans.append(table[i])
        return ans


        