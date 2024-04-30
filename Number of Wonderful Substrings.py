class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = {0: 1}  # Initialize the count dictionary with 0
        mask = 0
        result = 0
        for c in word:
            # Toggle the bit corresponding to the position of c in the alphabet
            mask ^= 1 << (ord(c) - ord('a'))
            # Increment result if mask is a palindrome
            result += count.get(mask, 0)
            # Increment result for each character with exactly one bit set in mask
            for i in range(10):
                result += count.get(mask ^ (1 << i), 0)
            # Update the count dictionary
            count[mask] = count.get(mask, 0) + 1
        return result
