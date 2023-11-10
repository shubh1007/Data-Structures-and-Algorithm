class Solution:
    def findClosestElements(self, a: List[int], k: int, x: int) -> List[int]:
        out = []
        n = len(a)
        
        def linSrch(num: int) -> int:
            nonlocal a
            ptr = 0
            while ptr < n - 1 and a[ptr] <= num:
                ptr += 1
            return ptr
        
        rEnd, lEnd = False, False
        
        l = r = linSrch(x)
        if l - 1 >= 0:
            if abs(a[l - 1] - x) <= abs(a[l] - x):
                l = r = l - 1
        out.append(a[l])
        count = 1
        l -= 1
        r += 1
        if l < 0:
            lEnd = True
        if r >= n:
            rEnd = True
        
        while count < k:
            if lEnd:
                while count < k:
                    out.append(a[r])
                    r += 1
                    if r == n:
                        count = k
                        break
                    count += 1
            elif rEnd:
                while count < k:
                    out.insert(0, a[l])
                    l -= 1
                    if l == -1:
                        count = k
                        break
                    count += 1
            else:
                dist1 = abs(a[l] - x)
                dist2 = abs(a[r] - x)
                if dist2 < dist1:
                    out.append(a[r])
                    r += 1
                    if r == n:
                        rEnd = True
                else:
                    out.insert(0, a[l])
                    l -= 1
                    if l < 0:
                        lEnd = True
                count += 1
                
        return out
