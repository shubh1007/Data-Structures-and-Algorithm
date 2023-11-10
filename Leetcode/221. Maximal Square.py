class Solution:
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                res = max(res, matrix[i][j])
        for row in reversed(range(m - 2)):
            for col in reversed(range(n - 2)):
                if matrix[row][col] == 1:
                    matrix[row][col] += min(matrix[row + 1][col],
                                        matrix[row][col + 1], matrix[row + 1][col + 1])
                    if matrix[row][col] > res:
                        res = matrix[row][col]
        return res * res


sol = Solution()
matrix = [["0", "1"], ["1", "0"]]
res = sol.maximalSquare(matrix)
print(res)
