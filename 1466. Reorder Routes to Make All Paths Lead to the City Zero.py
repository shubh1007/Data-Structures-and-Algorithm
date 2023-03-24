from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]):
        graph = { (a, b) for a, b in connections}
        neighbors = { i: [] for i in range(n)}
        visited = set()
        changes = 0
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        def dfs(node):
            nonlocal graph, neighbors, visited, changes
            for neighbor in neighbors[node]:
                if neighbor in visited:
                    continue
                if (neighbor, node) not in graph:
                    changes += 1
                visited.add(neighbor)
                dfs(neighbor)
        visited.add(0)
        dfs(0)
