class Solution:
    def minKBitFlips(self, nums, k):
        n = len(nums)
        flipCount = 0
        currentFlips = 0
        diff = [0] * (n + 1)  # diff array to track start and end of flips
        
        for i in range(n):
            currentFlips += diff[i]
            
            if (nums[i] + currentFlips) % 2 == 0:
                # Need a flip at position i
                if i + k > n:
                    return -1  # Cannot flip if the subarray exceeds boundary
                
                flipCount += 1
                currentFlips += 1
                diff[i + k] -= 1  # Mark the end of the flip effect
        
        return flipCount
