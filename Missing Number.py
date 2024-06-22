class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Compute the sum of the first n natural numbers
        expected_sum = n * (n + 1) // 2
        
        # Compute the sum of elements in nums
        actual_sum = sum(nums)
        
        # The missing number is the difference between expected_sum and actual_sum
        return expected_sum - actual_sum
