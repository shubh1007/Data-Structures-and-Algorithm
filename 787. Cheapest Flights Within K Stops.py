from sys import maxsize

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        Args:
            n (int): number of nodes
            flights (list[list[int]]): Connection array with weight
            src (int): source node
            dst (int): detination node
            k (int): Maximum Number of Stops between src and dst

        Returns:
            int: minimum price at which we can reach from source to destination with max k stop(s).
        """
        prices = [float("inf") for i in range(n)]
        prices[src] = 0
        for _ in range(k + 1):
            tempPrices = prices.copy()
            for source, destination, price in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + price < tempPrices[destination]:
                    tempPrices[destination] = prices[source] + price
            prices = tempPrices
        return -1 if prices[dst] == float("inf") else prices[dst]

n = 4
flights = [
    [0, 1, 100],
    [1, 2, 100],
    [2, 0, 100],
    [1, 3, 600],
    [2, 3, 200],
    ]
src = 0
dst = 3
k = 1

sol = Solution()
res = sol.findCheapestPrice(n, flights, src, dst, k)
print(res)
















