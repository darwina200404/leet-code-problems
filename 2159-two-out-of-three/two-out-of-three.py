class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """

        nums=list(set(nums1))+list(set(nums2))+list(set(nums3))
        answer=[]
        freq={}
        for item in nums:
            freq[item]=freq.get(item,0)+1
        answer=[key for key, value in freq.items()if value>=2]
        return answer
        
        