class BSTIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
    def next(self) -> int:
        result = self.stack.pop()
        curr = result.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return result.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0