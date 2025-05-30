class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_word=set(allowed)
        count=0
        for word in words:
            if all(char in allowed_word for char in word):
                count+=1
        return count

        