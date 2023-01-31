# UNSOLVED SOLUTION REVISITED

class Solution:
    def putMarbles(self, weights, k):
        n = len(weights)
        seq = [0 for i in range(n - 1)]
        for i in range(n - 1):
            seq[i] = weights[i] + weights[i + 1]
        seq.sort()
        ans = 0
        for i in range(k - 1):
            ans += seq[n - 2 - i] - seq[i]
        return ans

weights = [1,4,2,5,2]
k = 3
sol = Solution()
res = sol.putMarbles(weights, k)
print(res)





# class Solution {
# public:
#     long long putMarbles(vector<int>& A, int k) {
#         typedef long long LL;
#         int n = A.size();
#         vector<int> seq(n - 1);
#         for(int i = 0; i + 1 < n; ++i)
#             seq[i] = A[i] + A[i + 1];
#         sort(seq.begin(), seq.end());
#         LL ans = 0;
#         for(int i = 0; i + 1 < k; ++i)
#             ans += seq[n - 2 - i] - seq[i];
#         return ans;
#     }
# };