class Solution:
    def validPath(self, n, edges, source, destination):
        visited = set()
        graph = {}
        for i in range(n):
            graph[i] = []
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        def helper(source, destination):
            if source == destination: return True
            if (source, destination) not in visited:
                visited.add((source, destination))
                for neighbour in graph[source]:
                    hasPath = helper(neighbour, destination)
                    if hasPath: return True
                return False
        return helper(source, destination)

n = 10
edges = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
source = 7
destination = 5

sol = Solution()
res = sol.validPath(n, edges, source, destination)
print(res)