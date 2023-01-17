def solution(A, B, N):
    A = A + B
    A.sort()
    min_diff = max(A) - min(A)
    for i in range(N + 1):
        min_diff = min(min_diff, A[i + N - 1] - A[i])
    return min_diff

n = int(input())
res = []
for testcase in range(n):
    N = int(input())   
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # N = 4
    # A = [2, 1, 4, 3]
    # B = [3, 2, 6, 2]
    res.append(solution(A, B, N))
for i in res:
    print(i)


