class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        row_length=len(accounts)
        col_length=len(accounts[0])
        max_sum=0
        for i in range(row_length):
            Sum=0
            for j in range(col_length):
                Sum+=accounts[i][j]
            max_sum=max(Sum,max_sum)
        return max_sum
        