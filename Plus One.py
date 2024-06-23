class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # If we're here, it means all digits were 9
        # Need to prepend a 1 at the start
        return [1] + digits
