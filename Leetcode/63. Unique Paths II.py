class Solution:
    def uniquePathsWithObastacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        hashMap = {}
        def traverse(i, j):
            if (i, j) in hashMap: return hashMap[(i, j)]
            if i == m or j == n: return 0
            if obstacleGrid[i][j] == 1: 
                hashMap[(i, j)] = 0
                return hashMap[(i, j)]
            if i == m - 1 and j == n - 1: return 1
            right = traverse(i, j + 1)
            bottom = traverse(i + 1, j)
            hashMap[(i, j)] = right + bottom
            return hashMap[(i, j)]
        return traverse(0, 0)

obstacleGrid = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
sol = Solution()
result = sol.uniquePathsWithObastacles(obstacleGrid)
print(result)