class Solution:
    def monkeyMove(self, n):
        mod = 10**9 + 7
        total_ways = pow(2,n,mod)
        return (total_ways - 2) % mod
        # if n <= 1: return 0
        # MOD = 10 ^ 9 + 7
        # def pow(a, b):
        #     res = 1
        #     while b > a:
        #         if b % a == 1:
        #             res = res * a % MOD
        #         a = a * a % MOD
        #         b //= 2
        #     return res
        
        

        # return (pow(2, n) - (factorial(n-1))) % MOD

sol = Solution()
n = 4
res = sol.monkeyMove(n)
print(res)