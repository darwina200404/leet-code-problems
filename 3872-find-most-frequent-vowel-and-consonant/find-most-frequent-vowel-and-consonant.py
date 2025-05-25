class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq=Counter(s)
        vowel=['a','e','i','o','u']
        maxVowel,maxConstant=0,0
        for key,value in freq.items():
            if key in vowel:
                maxVowel=max(value,maxVowel)
            else:
                maxConstant=max(value,maxConstant)
        return maxVowel+maxConstant


        