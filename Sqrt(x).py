class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # right is the largest integer such that right^2 <= x
