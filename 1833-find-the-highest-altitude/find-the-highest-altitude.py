class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        max_alltitude=0
        alltitude=0
        for i in range(len(gain)):
            alltitude+=gain[i]
            max_alltitude=max(alltitude,max_alltitude)

        return max_alltitude


        