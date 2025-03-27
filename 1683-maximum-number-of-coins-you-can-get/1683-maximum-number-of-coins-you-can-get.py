class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)  
        n = len(piles) // 3  
        coin = 0


        for i in range(1, 2 * n, 2):  
            coin += piles[i]  

        return coin        




        