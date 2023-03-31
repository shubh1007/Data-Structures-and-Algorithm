from typing import List
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                for c in range(k, 0, -1):
                    dp[i][j][c] = 1 if c == 1 else 0
                    for x in range(i + 1, m + 1):
                        if pizza[x - 1][j] == 'A':
                            dp[i][j][c] += dp[x][j][c - 1]
                            break
                    for y in range(j + 1, n + 1):
                        if pizza[i][y - 1] == 'A':
                            dp[i][j][c] += dp[i][y][c - 1]
                            break
        return dp[0][0][k] % (10 ** 9 + 7)