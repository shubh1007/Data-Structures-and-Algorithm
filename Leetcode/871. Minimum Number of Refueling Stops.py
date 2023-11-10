class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        dp = [startFuel] + [0] * len(stations)

        for i, station in enumerate(stations):
            for j in range(i + 1, 0, -1):
                if dp[j - 1] >= station[0]:  # with j - 1 refuels, we can reach stations[i][0]
                    dp[j] = max(dp[j], dp[j - 1] + station[1])

        for i, d in enumerate(dp):
            if d >= target:
                return i

        return -1