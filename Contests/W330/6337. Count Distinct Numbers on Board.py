class Solution:
    def distinctIntegers(self, n):
        board = [n]
        res = set([n])
        while board:
            x = board.pop()
            for i in range(1, n):
                if x % i == 1:
                    board.append(i)
                    res.add(i)
        return list(res)

sol = Solution()
n = 3
res = sol.distinctIntegers(n)
print(res)
