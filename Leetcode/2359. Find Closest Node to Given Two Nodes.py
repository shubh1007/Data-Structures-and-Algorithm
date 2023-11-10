class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [-1 for i in range(n)]
        dist2 = [-1 for i in range(n)]
        visited = set()
        def dfs(node, dist, distance):
            if node == -1: return
            if node not in visited:
                dist[node] = distance
                visited.add(node)
                dfs(edges[node], dist, distance + 1)
        
        dfs(node1, dist1, 0)
        visited = set()
        dfs(node2, dist2, 0)
        result = -1
        answer = n
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                if max(dist1[i], dist2[i]) < answer:
                    answer = max(dist1[i], dist2[i])
                    result = i
        return result