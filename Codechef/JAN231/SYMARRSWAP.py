# def solution(A, B, N):
#     A.sort()
#     B.sort()
#     res = float("inf")
#     for i in range(N):
#         diff = max(A[i], B[N - i - 1] - min(A[i], B[N - i - 1]))
#         res = min(res, diff)
#     return res
        
# n = int(input())
# for testcase in range(n):
#     N = int(input())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     res = solution(A, B, N)
#     print(res)