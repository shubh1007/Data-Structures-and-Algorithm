class Solution:
    def minTime(self, n, edges, hasApple):
        def dfs(node, parent, adj, hasApple):
            totalTime = 0
            childTime = 0
            for child in adj[node]:
                if child == parent:
                    continue
                childTime = dfs(child, node, adj, hasApple)
                if childTime or hasApple[child]:
                    totalTime += childTime + 2
            return totalTime
        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return dfs(0, -1, adj, hasApple)


n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]
sol = Solution()
res = sol.minTime(n, edges, hasApple)
print(res)
