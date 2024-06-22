class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] will store the size of largest subset ending with nums[i]
        prev = [-1] * n  # prev[i] will store the index of previous element in the subset
        
        max_size = 1
        max_idx = 0
        
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            
            if dp[i] > max_size:
                max_size = dp[i]
                max_idx = i
        
        # Build the largest subset
        subset = []
        while max_idx != -1:
            subset.append(nums[max_idx])
            max_idx = prev[max_idx]
        
        return subset
