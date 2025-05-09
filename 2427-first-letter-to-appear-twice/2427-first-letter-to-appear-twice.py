class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=set()
        for i in s:
            if i not in a:
                a.add(i)
            else:
                return i
        return 0