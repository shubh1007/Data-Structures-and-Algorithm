class Solution:
    def allPathsSourceTarget(self, graph):
        res = []        
        n = len(graph)
        def dfs(node, ds):
            if node == (n - 1): 
                res.append(ds.copy())
                return
            for neighbour in graph[node]:
                ds.append(neighbour)
                dfs(neighbour, ds)
                ds.pop()
        dfs(0, [0])
        return res
    
graph = [[4,3,1],[3,2,4],[3],[4],[]]
sol = Solution()
res = sol.allPathsSourceTarget(graph)
print(res)

                
