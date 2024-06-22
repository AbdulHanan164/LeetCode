class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        const int MOD = 1000000007;
        vector<vector<vector<int>>> dp(maxMove + 1, vector<vector<int>>(m, vector<int>(n, 0)));
        dp[0][startRow][startColumn] = 1;
        int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int count = 0;
        
        for (int move = 1; move <= maxMove; ++move) {
            for (int r = 0; r < m; ++r) {
                for (int c = 0; c < n; ++c) {
                    for (auto& dir : directions) {
                        int prevR = r + dir[0];
                        int prevC = c + dir[1];
                        if (prevR < 0 || prevR >= m || prevC < 0 || prevC >= n) {
                            count = (count + dp[move - 1][r][c]) % MOD;
                        } else {
                            dp[move][r][c] = (dp[move][r][c] + dp[move - 1][prevR][prevC]) % MOD;
                        }
                    }
                }
            }
        }
        
        return count;
    }
};
