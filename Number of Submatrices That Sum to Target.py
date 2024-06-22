class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int count = 0;
        
        // Compute prefix sums
        vector<vector<int>> prefix(rows + 1, vector<int>(cols + 1, 0));
        for (int i = 1; i <= rows; ++i) {
            for (int j = 1; j <= cols; ++j) {
                prefix[i][j] = matrix[i - 1][j - 1] +
                               prefix[i - 1][j] +
                               prefix[i][j - 1] -
                               prefix[i - 1][j - 1];
            }
        }
        
        // Iterate over all possible pairs of rows (top, bottom)
        for (int top = 1; top <= rows; ++top) {
            for (int bottom = top; bottom <= rows; ++bottom) {
                unordered_map<int, int> countMap;
                countMap[0] = 1; // This handles the case when the entire row contributes to the sum
                int currentSum = 0;
                
                // Iterate over each column and calculate the sum of elements from top to bottom
                for (int col = 1; col <= cols; ++col) {
                    currentSum = prefix[bottom][col] - prefix[top - 1][col];
                    
                    if (countMap.find(currentSum - target) != countMap.end()) {
                        count += countMap[currentSum - target];
                    }
                    
                    countMap[currentSum]++;
                }
            }
        }
        
        return count;
    }
};
