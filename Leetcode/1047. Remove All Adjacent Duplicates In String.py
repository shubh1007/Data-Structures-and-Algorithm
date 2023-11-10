class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        idx = 0
        while idx < len(s):
            if len(res) == 0:
                res.append(s[idx])
            elif res[-1] == s[idx]:
                res.pop(-1)
            else:
                res.append(s[idx])
            idx += 1
        return "".join(x for x in res)
            
        
