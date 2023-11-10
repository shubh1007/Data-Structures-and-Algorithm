class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        if n < 3:
            return 0 if n == 0 else 1
        t3 = t0 + t1 + t2
        for _ in range(n - 2):
            t3 = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = t3
        return t3