# You are given an array A consisting of N integers. You want to make all the elements of the given array A equal by performing below operations zero or more times.Operation: Select an index i (1 <= i<=N) and change A[i} to floor(A[i]/2). 
# Determine the minimum number of operations you need to perform to make all the elements of array A equal


def solve(N, A):
    if N == 1:
        return 0
    def gcd(x, y):
        x, y = max(x, y), min(x, y)
        while y:
            x, y = y, x % y
        return x
    num1 = A[0] 
    num2 = A[1]
    GCD = gcd(num1, num2)
    for i in range(2, N):
        GCD = gcd(GCD, A[i])
    res = 0
    for i in range(N):
        while A[i] > GCD:
            A[i] //= 2
            res += 1
    return res

N = 7
A = [8, 10, 19, 14, 12, 2, 9]
print(solve(N, A))







# A = [3, 3, 5]
# min_element = min(A)
# operations = 0
# for i in range(len(A)):
#     while A[i] > min_element:
#         A[i] //= 2
#         operations += 1
# print(A)
# print(operations)