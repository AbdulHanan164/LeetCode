from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Dictionary to store indices of numbers

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

        # No solution found
        return []


# Test cases
sol = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(sol.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(sol.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(sol.twoSum(nums3, target3))  # Output: [0, 1]
