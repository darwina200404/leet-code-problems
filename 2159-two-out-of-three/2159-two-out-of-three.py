class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        a=list(set(nums1))
        b=list(set(nums2))
        c=list(set(nums3))
        nums=a+b+c
        answer=[]
        freq={}
        for item in nums:
            freq[item]=freq.get(item,0)+1
        answer=[key for key, value in freq.items()if value>=2]
        return answer
        
        