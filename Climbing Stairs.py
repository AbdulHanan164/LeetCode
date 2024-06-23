class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 1 way to be on the ground
        dp[1] = 1  # Base case: 1 way to reach the first step
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
