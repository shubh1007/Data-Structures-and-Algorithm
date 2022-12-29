import heapq


class Solution:
    def getOrder(self, tasks):
        for idx, task in enumerate(tasks):
            task.append(idx)
        tasks.sort(key=lambda t: t[0])
        heapq.heapify(tasks)
        res = []
        HEAP = []
        time = tasks[0][0]
        idx = 0
        while HEAP or idx < len(tasks):
            while idx < len(tasks) and time >= tasks[idx][0]:
                heapq.heappush(HEAP, tasks[idx][1:])
                idx += 1
            if not HEAP:
                time = tasks[idx][0]
            else:
                procTime, index = heapq.heappop(HEAP)
                time += procTime
                res.append(index)
        return res


sol = Solution()
tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
res = sol.getOrder(tasks)
print(res)
