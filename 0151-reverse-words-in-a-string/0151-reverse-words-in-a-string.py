class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        a.reverse()
        s=' '.join(a)
        return s
        