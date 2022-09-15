class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        cnt, ans = Counter(changed), []
        for num in sorted(changed, key = lambda x: abs(x)):
            if cnt[num] == 0: continue
            if cnt[2*num] == 0: return []
            ans += [num]
            if num == 0 and cnt[num] <= 1: return []
            cnt[num] -= 1
            cnt[2*num] -= 1
        
        return ans
