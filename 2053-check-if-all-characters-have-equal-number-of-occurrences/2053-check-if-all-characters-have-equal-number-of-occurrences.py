class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq={}
        for item in s:
            freq[item]=freq.get(item,0)+1
        values = list(freq.values())
        return all(v == values[0] for v in values)


            




        