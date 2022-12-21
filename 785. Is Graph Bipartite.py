class Solution:
    def isBipartite(self, graph):
        mygraph = {}
        n = len(graph) - 1
        for i in range(n):
            mygraph[i] = []
        for node in range(n):
            for neighbour in graph[node]:
                mygraph[node].append(neighbour)
        colors = [-1] * (n + 1)
        def bfs(source):
            Q = [source]
            colors[source] = 0
            while Q:
                node = Q.pop(0)
                for neighbour in graph[node]:
                    if colors[neighbour] == colors[node]:
                        return False
                    if colors[neighbour] == -1:
                        colors[neighbour] = 1 - colors[node]
                        Q.append(neighbour)
            return True
        for i in range(n):
            if colors[i] == -1:
                if not bfs(i):
                    return False
        return True


graph = [
    [1,2,3],
    [0,2],
    [0,1,3],
    [0,2]]
sol = Solution()
res = sol.isBipartite(graph)
print(res)