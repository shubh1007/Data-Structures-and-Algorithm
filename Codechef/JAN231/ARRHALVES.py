n = int(input())
for testcase in range(n):
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    v = []
    r = []
    for i in range(1, N + 1):
        if A[i] > N:
            v.append(i)
    for i in range(N + 1, 2 * N + 1):
        if A[i] <= N:
            r.append(i)
    v.insert(0, 0)
    r.insert(0, 0)
    m = 1
    c = 0
    i = len(v) - 1
    for i in reversed(range(1, len(v))):
        x = N - v[i]
        y = r[m] - n - 1
        c += x + y + 1
        m += 1
    print(c)

# A = 3 2 1 4
# B = 3 2 1 4
# B = 1 2 3 4 Sorted
# target = B[1] = 2
# 