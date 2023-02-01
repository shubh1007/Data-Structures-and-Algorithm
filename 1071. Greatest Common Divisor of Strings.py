class Solution:
    def gcdofStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        def isValid(k):
            if l1 % k or l2 % k: return False
            n1, n2 = l1 // k, l2 //k
            base = str1[: k]
            return str1 == n1 * base and str2 == n2 * base
        for i in range(min(l1, l2), 0, -1):
            if isValid(i):
                return str1[:i]
        return ""