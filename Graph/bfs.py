class Node:
    def __init__(self, val = 0, adjList = []) -> None:
        self.val = val
        self.adjList = adjList
        self.visited = False

class Graph:
    def __init__(self, nodes = []) -> None:
        self.nodes = nodes

    def bfs(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True
        while queue:
            node = queue.pop(0)
            print(node.val, end = ",")
            for adjNode in node.adjList:
                if not adjNode.visited:
                    queue.append(adjNode)
                    adjNode.visited = True

    def dfs(self, startNode):
        stack = []
        stack.append(startNode)
        while stack:
            node = stack.pop(0)
            if node.visited:
                continue
            print(node.val, end = ",")
            node.visited = True
            for adjNode in node.adjList:
                if not adjNode.visited:
                    stack.append(adjNode)
                    

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.adjList = [node2, node3]
    node2.adjList = [node1, node3]
    node3.adjList = [node1, node2]
    graph = Graph([node1, node2, node3])
    graph.bfs(node1)
    graph.dfs(node1)
