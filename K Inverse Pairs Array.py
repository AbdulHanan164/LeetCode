class Solution {
public:
    int kInversePairs(int n, int k) {
        const int MOD = 1000000007;
        
        // Initialize a 2D array for DP
        int dp[1001][1001] = {0}; // dp[i][j] represents the number of arrays of length i with exactly j inverse pairs
        
        // Base case: One way to have 0 inverse pairs with an array of length 0
        dp[0][0] = 1;
        
        // Fill the dp table
        for (int i = 1; i <= n; ++i) {
            dp[i][0] = 1; // Only one way to have 0 inverse pairs with any length i
            
            for (int j = 1; j <= k; ++j) {
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
                if (j >= i) {
                    dp[i][j] -= dp[i - 1][j - i];
                }
                dp[i][j] = (dp[i][j] + MOD) % MOD;
            }
        }
        
        return dp[n][k];
    }
};
