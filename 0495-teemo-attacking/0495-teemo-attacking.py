class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not  timeSeries:
            return 0
        total_duration=0
        for i in range(len(timeSeries)-1):
            total_duration+=min(duration,timeSeries[i + 1] - timeSeries[i])
        return total_duration + duration