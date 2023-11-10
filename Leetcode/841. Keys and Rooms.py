class Solution:
    def canVisitAllRooms(self, rooms):
        res = {}
        for i in range(len(rooms)): res[i] = False
        stack = [0]
        while stack:
            temp = stack.pop()
            if not res[temp]:
                res[temp] = True
                for i in rooms[temp]:
                    if not res[i]:
                        stack.append(i)
        for i in res.values():
            if not i: 
                print(i)
                return False
        return True

sol = Solution()
rooms = [[1],[2],[3],[]]
res = sol.canVisitAllRooms(rooms)
print(res)


