"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(x1, y1, x2, y2):
            if (x1 == x2 and y1 == y2):
                return Node(grid[x1][y1], True, None, None, None, None)
            midX, midY = (x1+x2)//2, (y1+y2)//2
            topleft = build(x1, y1, midX, midY)
            topright = build(x1, midY + 1, midX, y2)
            bottomleft = build(midX + 1, y1, x2, midY)
            bottomright = build(midX + 1, midY + 1, x2, y2)
            
            if (topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and topleft.val == topright.val == bottomleft.val == bottomright.val):
                return Node(topleft.val, True, None, None, None, None)
            else:
                return Node(None, False, topleft, topright, bottomleft, bottomright)

        n = len(grid)
        if n == 0: return None
        return build(0, 0, n-1, n-1)