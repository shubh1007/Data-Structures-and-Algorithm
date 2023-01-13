from collections import defaultdict


class Solution:
    def longestPath(self, parent, s):
        graph = defaultdict(list)
        for i, j in enumerate(parent):
            graph[j].append(i)
        self.result = 1

        def dfs(node):
            long = seclong = 0
            for child in graph[node]:
                path_length = dfs(child)
                if s[child] != s[node]:
                    if path_length > long:
                        seclong = long
                        long = path_length
                    elif path_length > seclong:
                        seclong = path_length
            self.result = max(self.result, long + seclong + 1)
            return long + 1
        dfs(0)
        return self.result



sol = Solution()
parent = [-1, 0, 0, 0]
s = "acba"
res = sol.longestPath(parent, s)
print(res)
