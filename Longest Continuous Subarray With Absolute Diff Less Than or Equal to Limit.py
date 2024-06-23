from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        max_deque = deque()  # to store indices of maximum values in current window
        min_deque = deque()  # to store indices of minimum values in current window
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Update max_deque with current right pointer
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Update min_deque with current right pointer
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Check the condition |max(nums[i:j+1]) - min(nums[i:j+1])| <= limit
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update max_length with the current valid window size
            max_length = max(max_length, right - left + 1)
        
        return max_length
