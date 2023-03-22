from typing import List
from sys import maxsize
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for i in range(1, n + 1):
            graph[i] = []
        for start, end, cost in roads:
            graph[start].append([end, cost])
            graph[end].append([start, cost])
        visited = set()
        self.res = maxsize
        def dfs(node):
            self.res = min(self.res, node[1])
            if node[0] in visited: return 
            visited.add(node[0])
            
            for neighbour in graph[node[0]]:
                dfs(neighbour)
        dfs([1, maxsize])
        return self.res