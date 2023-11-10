from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        res = 0
        while left <= right:
            SUM = people[left] + people[right]
            if SUM <= limit:
                res += 1
                left += 1
                right -= 1
            else:
                res += 1
                right -= 1
        return res

if __name__ == '__main__':
    people = [1, 2]
    limit = 3
    print(Solution().numRescueBoats(people, limit))
