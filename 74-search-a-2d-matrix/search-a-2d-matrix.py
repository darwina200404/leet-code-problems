class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        while (left<=right):
            mid=left+(right-left)//2
            midrow,midcol=divmod(mid,n)
            if matrix[midrow][midcol]==target:
                return 1
            elif matrix[midrow][midcol]<target:
                left=mid+1
            else:
                right=mid-1

    
        return 0
        