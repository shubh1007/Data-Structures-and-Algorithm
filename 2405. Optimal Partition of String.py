class Solution:
    def partitionString(self, s: str) -> int:
        hashset = set()
        res = 0
        for char in s:
            if char in hashset:
                res += 1
                hashset = set()
            hashset.add(char)
        return res + 1

sol = Solution()
s = "shubham"
res = sol.partitionString(s)
print(res)

Output:
# 2
