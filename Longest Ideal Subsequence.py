class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26  # dp[i] stores the length of the longest ideal string ending with letter i
        for char in s:
            char_index = ord(char) - ord('a')
            # Find the maximum length of ideal strings ending with letters within k distance
            max_len = 0
            for i in range(max(0, char_index - k), min(26, char_index + k + 1)):
                max_len = max(max_len, dp[i])
            dp[char_index] = max_len + 1  # Extend the ideal string with the current character
        return max(dp)  # Return the maximum length found