# USING BFS
def cycleDetection(graph, n):
    visited = [False] * n
    parent = [-1] * n
    queue = []
    for i in range(n):
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
            while queue:
                node = queue.pop(0)
                for j in graph[node]:
                    if visited[j] == False:
                        queue.append(j)
                        visited[j] = True
                        parent[j] = node
                    elif parent[node] != j:
                        return True
    return False

