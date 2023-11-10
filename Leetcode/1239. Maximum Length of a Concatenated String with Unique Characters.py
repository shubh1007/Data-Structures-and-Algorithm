class Solution(object):

    def maxLength(self, arr):

        """

        :type arr: List[str]

        :rtype: int

        """

        self.ans = 0

        flags = [False for _ in range(26)]

        self.dfs(arr, flags)

        return self.ans

    def dfs(self, arr, flags):

        for i in range(len(arr)):

            prev_flags = flags[:]

            flag = True

            for c in arr[i]:

                if flags[ord(c) - ord('a')]:

                    flag = False

                    break

                else:

                    flags[ord(c) - ord('a')] = True

            if flag:

                self.ans = max(self.ans, sum(flags))

                self.dfs(arr[i + 1:], flags) 

            flags = prev_flags[:]

        
