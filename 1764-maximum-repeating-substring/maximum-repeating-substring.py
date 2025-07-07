class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count=0
        while True:
            if word*(count+1) not in sequence:
                return count
            count+=1
        
        