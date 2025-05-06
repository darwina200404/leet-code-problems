class Solution(object):
    def getValue(self,word):
        elements=[]
        freq={}
        for item in word:
            freq[item]=freq.get(item,0)+1
        elements=[key for key,value in freq.items()if value==1]
        return elements
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        count=0
        lis1=self.getValue(words1)
        lis2=self.getValue(words2)
        for item in lis1:
            if item in lis2:
                count+=1
        return count




        