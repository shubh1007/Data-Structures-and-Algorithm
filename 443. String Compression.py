from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        res = ""
        count = 1
        i = 1
        while i < len(chars):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                if count == 1: 
                    res += chars[i - 1] 
                else:
                    res += chars[i - 1] + str(count)
                count = 1
            i += 1
        if count == 1:
            res += chars[i - 1]
        else:
            res += chars[i - 1] + str(count)
        for i in range(len(res)):
            chars[i] = res[i]
        print(chars)
        return len(res)




