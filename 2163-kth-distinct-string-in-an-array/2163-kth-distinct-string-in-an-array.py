class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        freq={}
        for item in arr:
            freq[item]=freq.get(item,0)+1
        element=[item for item in arr if freq[item] == 1]
        if k<=len(element):
            return element[k-1]
        return ""
        
        