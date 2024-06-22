class Solution(object):
    def sequentialDigits(self, low, high):
        result = []
        for start in range(1, 10):
            num = start
            while num <= high:
                if num >= low:
                    result.append(num)
                last_digit = num % 10
                if last_digit == 9:
                    break
                num = num * 10 + (last_digit + 1)
        
        return sorted(result)
