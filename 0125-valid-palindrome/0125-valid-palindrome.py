class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s=s.lower()
        s = ''.join(c for c in s if c.isalnum())
        rev=s[::-1]
        return rev==s
        