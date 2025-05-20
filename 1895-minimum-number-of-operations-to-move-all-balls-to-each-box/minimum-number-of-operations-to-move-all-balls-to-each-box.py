class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        res = [0] * n
        
        count = 0
        ops = 0
        
        for i in range(n):
            res[i] += ops
            count += int(boxes[i])
            ops += count

        count = 0
        ops = 0
        
        for i in range(n-1, -1, -1):
            res[i] += ops
            count += int(boxes[i])
            ops += count
        
        return res





