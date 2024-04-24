class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        # Initialize tribonacci values for n = 0, 1, and 2
        t0, t1, t2 = 0, 1, 1
        # Calculate tribonacci for n > 2
        for _ in range(3, n + 1):
            tn = t0 + t1 + t2
            t0, t1, t2 = t1, t2, tn
        return t2
