class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)  # Convert string to list (since strings are immutable in Python)
        left, right = 0, len(s) - 1  # Initialize two pointers
        
        while left < right:
            # Move left pointer until it finds a vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer until it finds a vowel
            while left < right and s[right] not in vowels:
                right -= 1
            # Swap the vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)  # Convert list back to string

        