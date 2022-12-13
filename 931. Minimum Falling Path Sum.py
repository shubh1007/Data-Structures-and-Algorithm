class Solution:
    def minFallingPathSum(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                l = matrix[i][j - 1] if j - 1 >=0 else float("inf")
                c = matrix[i - 1][j] 
                r = matrix[i - 1][j + 1] if j + 1 < len(matrix[0]) else float("inf")
                matrix[i][j] += min(l, c, r)
        return min(matrix[-1])

matrix = [[2,1,3],[6,5,4],[7,8,9]]
sol = Solution()
res = sol.minFallingPathSum(matrix)
print(res)