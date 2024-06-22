class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        
        # Step 1: Initialize the dp array for single characters and adjacent pairs
        dp = [[False] * n for _ in range(n)]
        count = 0
        
        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        # Check adjacent pairs
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        
        # Step 2: Expand around centers for substrings of length > 2
        for length in range(3, n + 1):  # length of substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1
        
        return count
