class Solution(object):
    def searchRange(self, nums, target):
        def find_leftmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def find_rightmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_index = find_leftmost(nums, target)
        right_index = find_rightmost(nums, target)
        
        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]
