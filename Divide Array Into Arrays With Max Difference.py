class Solution(object):
    def divideArray(self, nums, k):
        n = len(nums)
        if n % 3 != 0:
            return []  # Not possible to divide if not multiple of 3
        
        nums.sort()
        result = []
        i = 0
        while i < n:
            if i + 2 < n and nums[i+2] - nums[i] <= k:
                result.append([nums[i], nums[i+1], nums[i+2]])
                i += 3
            else:
                return []  # No valid triplet found
            
        return result
