class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @param D : list of integers
    # @return an integer
    def solve(self, A, B, C, D):
        def dfs(node, parent, graph, dp, D):
            is_leaf = True
            for child in graph[node]:
                if child != parent:
                    is_leaf = False
                    dfs(child, node, graph, dp, D)
                    dp[node][0] += min(dp[child][0], dp[child][1])
                    dp[node][1] += dp[child][0]
            if is_leaf:
                dp[node][0] = D[node]
                dp[node][1] = D[node]//2
        MOD = 10 ** 9 + 7
        graph = [[] for _ in range(A)]
        for u, v in B:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        dp = [[0, 0] for _ in range(A)]
        dfs(0, -1, graph, dp, D)
        ans = 0
        for u, v in C:
            ans += min(dp[u - 1][0], dp[u - 1][1]) + min(dp[v - 1][0], dp[v - 1][1])
        return ans % MOD

sol = Solution()
A = 5