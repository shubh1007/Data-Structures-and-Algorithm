class Solution:
    def minimumRounds(self, tasks):
        """Returns the number of rounds required to complete all the tasks. 
        It takes 2 or 3 tasks at a time.

        Args:
            tasks (List[int]): List of tasks in unsorted order
        """
        # Count the frequency of elements.
        # Sort the values on the basis of their count.
        # set rounds = 0
        # loop through the count list
        #   temp = count.pop()
        #   if temp == 1:
        #       return -1
        #   elif temp is divisible by 3:
        #       rounds += temp / 3
        #   elif temp is divisible by 2:
        #       rounds += temp / 2
        #   elif temp is greater than 3:
        #       rounds += temp // 3
        #       temp = temp % 3
        #       if temp % 3 == 0 or temp % 2 == 0:
        #           count.append(temp)

        hm = {}
        for i in tasks:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        count = list(hm.values())
        rounds = 0
        for i in count:
            if i == 1: return -1
            elif i % 3== 0:
                rounds += i // 3
            else:
                rounds += (i // 3) + 1
        return rounds



sol = Solution()
tasks = [69, 65, 62, 64, 70, 68, 69, 67, 60, 65, 69, 62, 65, 65, 61, 66, 68, 61, 65, 63, 60, 66, 68, 66,
         67, 65, 63, 65, 70, 69, 70, 62, 68, 70, 60, 68, 65, 61, 64, 65, 63, 62, 62, 62, 67, 62, 62, 61, 66, 69]
res = sol.minimumRounds(tasks)
print(res)
