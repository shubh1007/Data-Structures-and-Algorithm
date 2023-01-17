n = int(input())
for i in range(n):
    X1, Y1, X2, Y2 = list(map(int, input().split()))
    d1 = X1**2 + Y1**2
    d2 = X2**2 + Y2**2
    if d1 < d2: print("BOB")
    elif d1 > d2: print("ALICE")
    else: print("EQUAL")

