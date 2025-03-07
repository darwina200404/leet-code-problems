class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # Position to write compressed characters
        i = 0  # Read pointer

        while i < len(chars):
            char = chars[i]  # Store the current character
            count = 0  # Count how many times it appears

            # Count occurrences of chars[i]
            while i < len(chars) and chars[i] == char:
                count += 1
                i += 1  # Move read pointer forward

            # Write the character
            chars[write] = char
            write += 1

            # Write the count only if it's greater than 1
            if count > 1:
                for c in str(count):  # Convert number to characters
                    chars[write] = c
                    write += 1

        return write


        