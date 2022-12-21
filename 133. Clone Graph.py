class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        cloneGraph = {}
        def clone(node):
            if node in cloneGraph:
                return cloneGraph[node]
            cloneNode = Node(node.val)
            cloneGraph[node] = cloneNode
            for neighbor in node.neighbors:
                cloneNode.neighbors.append(clone(neighbor))
            return cloneNode
        return clone(node) if node else None

        