class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> oddIndices;
        
        // Step 1: Identify indices of odd numbers
        for (int i = 0; i < n; ++i) {
            if (nums[i] % 2 != 0) {
                oddIndices.push_back(i);
            }
        }
        
        // Step 2: Handle cases with fewer than k odd numbers
        if (oddIndices.size() < k) {
            return 0;
        }
        
        // Step 3: Calculate number of valid subarrays
        int count = 0;
        
        // Sliding window approach
        for (int i = 0; i <= oddIndices.size() - k; ++i) {
            int left = i;
            int right = i + k - 1;
            
            int leftCount = (left == 0) ? oddIndices[left] + 1 : oddIndices[left] - oddIndices[left - 1];
            int rightCount = (right + 1 < oddIndices.size()) ? oddIndices[right + 1] - oddIndices[right] : n - oddIndices[right];
            
            count += leftCount * rightCount;
        }
        
        return count;
    }
};
