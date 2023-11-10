class Solution:
    def strStr(self, stack: str, needle: str) -> int:
        if needle is None or stack is None: return -1
        if needle == stack: return 0
        for i in range(len(stack) - len(needle) + 1):
            if stack[i: i + len(needle)] == needle:
                return i
        return -1