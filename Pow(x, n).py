class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        
        if n < 0:
            x = 1 / x
            n = -n
        
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half
