class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False] * n
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        def dfs(node):
            visited[node] = True
            count = 1
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    count += dfs(neighbour)
            return count
        
        nodes = []
        for node in range(n):
            if not visited[node]:
                nodes.append(dfs(node))
        return sum([(n-c)*c for c in nodes])//2
            