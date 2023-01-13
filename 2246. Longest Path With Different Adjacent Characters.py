from collections import defaultdict

class Solution:
    def longestPath(self, parent, s):
        # Build a graph
        # define self.result variable that stores the result
        # Define DFS Function
            # set longest and second longest variable to 0
            # loop through all of its children
                # get path_length via recursion of child node
                # if s[child] != s[node]:
                    # if path_length > longest variable
                        # second_longest = longest
                        # longest = path_length
                    # elif path_length > second_longest
                        # second_longest = path_length 
            # set self.result = max(self.result, longest + second_longest + 1)
            # return longest + 1
        # call dfs function with node 0
        # return self.result
        self.result = 1
        graph = defaultdict(list)
        for idx, val in enumerate(parent):
            graph[val].append(idx)
        def dfs(node):
            longest, second_longest = 0, 0
            for child in graph[node]:
                path_length = dfs(child)
                if s[node] != s[child]:
                    if path_length > longest:
                        second_longest = longest
                        longest = path_length
                    elif path_length > second_longest:
                        second_longest = path_length
            self.result = max(self.result, longest + second_longest + 1)
            return longest + 1
        dfs(0)
        return self.result

sol = Solution()
parent = [-1, 0, 0, 0]
s = "acba"
res = sol.longestPath(parent, s)
print(res)
