class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n=len(candies)
        answer=[False]*n
        maximimum_candi=max(candies)
        for i in range(n):
            if(candies[i]+extraCandies>=maximimum_candi):
                answer[i]=True
        return answer
        