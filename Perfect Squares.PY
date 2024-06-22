class Solution(object):
    def numSquares(self, n):
        # Initialize dp array with a large number
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Zero perfect squares needed for sum 0
        
        # Compute minimum perfect squares for each number from 1 to n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]
