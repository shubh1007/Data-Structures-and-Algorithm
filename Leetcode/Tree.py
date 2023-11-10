from LevelOrderTraversal import TreeNode

class BST:
    def __init__(self, root = None):
        self.root = TreeNode(root)

    def insert(self, val):
        prev = None
        curr = self.root
        while curr:
            prev = curr
            if curr.val < val: curr = curr.right
            else: curr = curr.left
        newNode = TreeNode(val)
        if prev == None: self.root = newNode
        elif prev.val > val: prev.left = newNode
        else:
            prev.right = newNode
        
    def inOrder(self, root):
        if root == None:return
        self.inOrder(root.left)
        print(f"{root.val}", end = " ")
        self.inOrder(root.right)

root = BST(50)
list1 = [30, 20, 40, 70, 60, 80]
for i in list1:
    root.insert(i)

root.inOrder(root.root)


        
        
        
        
        
        
    

