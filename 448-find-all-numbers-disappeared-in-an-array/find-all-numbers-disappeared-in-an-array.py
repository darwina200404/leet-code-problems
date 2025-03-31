class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        n=len(nums)+1
        update_nums=set(nums)
        for i in range(1,n):
            if i not in update_nums:
                answer.append(i)
        return answer

        