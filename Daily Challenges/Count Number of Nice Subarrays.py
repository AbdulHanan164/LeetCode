class Solution(object):
    def numberOfSubarrays(self, nums, k):
        # Step 1: Create a binary array where 1 indicates odd numbers and 0 indicates even numbers
        binary = [1 if num % 2 != 0 else 0 for num in nums]
        
        # Step 2: Calculate prefix sum array of the binary array
        prefix_count = {}
        prefix_count[0] = 1  # Base case: 1 subarray with sum 0 (considering count of odd numbers)
        
        current_odd_count = 0
        count = 0
        
        for num in binary:
            current_odd_count += num
            if current_odd_count - k in prefix_count:
                count += prefix_count[current_odd_count - k]
            if current_odd_count in prefix_count:
                prefix_count[current_odd_count] += 1
            else:
                prefix_count[current_odd_count] = 1
        
        return count
