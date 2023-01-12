from collections import defaultdict


class Solution:
    def countSubTrees(self, n, edges, labels):
        tree = defaultdict(list)
        lcount = defaultdict(int)
        output = [0] * n
        for start, end in edges:
            tree[start].append(end)
            tree[end].append(start)

        def helper(node, parent):
            prev = lcount[labels[node]]
            lcount[labels[node]] += 1
            for child in tree[node]:
                if child != parent:
                    helper(child, node)
            output[node] = lcount[labels[node]]  - prev
        helper(0, None)
        return output


        # tree = defaultdict(list)
        # lcount = defaultdict(int)
        # self.output = [0] * n
        # for edge in edges:
        #     tree[edge[0]].append(edge[1])
        #     tree[edge[1]].append(edge[0])
        # def helper(i, parent):
        #     prev = lcount[labels[i]]
        #     lcount[labels[i]] += 1
        #     for child in tree[i]:
        #         if child != parent:
        #             helper(child, i)
        #     self.output[i] = lcount[labels[i]] - prev
        # helper(0, None)
        # return self.output
n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
labels = "abaedcd"
output = [2, 1, 1, 1, 1, 1, 1]
sol = Solution()
res = sol.countSubTrees(n, edges, labels)
print(res)
