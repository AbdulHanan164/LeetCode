class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        
        steps = 1
        max_reach = nums[0]
        current_end = nums[0]
        
        for i in range(1, len(nums)):
            if i > current_end:
                steps += 1
                current_end = max_reach
            max_reach = max(max_reach, i + nums[i])
        
        return steps
