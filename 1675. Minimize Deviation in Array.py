import heapq
class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        maxnums = [-(n * 2 if n & 1 else n) for n in nums]
        minn, maxx = -max(maxnums), -min(maxnums)
        mindev = maxx - minn

        heapq.heapify(maxnums)
        while not maxnums[0] & 1:
            maxtrans = maxnums[0] >> 1
            heapq.heapreplace(maxnums, maxtrans)
            minn = min(minn, -maxtrans)
            maxx = -maxnums[0]
            mindev = min(mindev, maxx - minn)

        return mindev