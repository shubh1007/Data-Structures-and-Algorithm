"""
arr = [1, 3, 2, 3, 4]
n = 5
1 - 4


n*(n-1)/2

sum(1,2,3,3,4) - sum(1,2,3,4) = 3

"""
def repeatFromOneToN(arr):
    sum1 = 0
    for i in arr:
        sum1 += i
    n = len(arr)

    sum2 = int(n*(n-1)/2)
    
    result = sum1 - sum2
    return result

arr = [1, 3, 2, 3, 4]
result = repeatFromOneToN(arr)
print(result)
exit()

def findTheOddOne(arr):
    xor = 0
    for i in arr:
        xor = xor^i
    return xor


"""
arr = [1,1,2,2,3,3,4,5]
result = findTheOddOne(arr)
print(result)
"""



exit()


def delete(arr, item):
    lb = 0
    ub = len(arr) - 1
    flag = -1
    while lb <= ub and flag == -1:
        mid = (lb+ub)//2
        if arr[mid] == item:
            flag = mid
            break
        elif arr[mid] < item:
            lb = mid + 1
        else:
            ub = mid - 1
    if flag == -1:
        return -1
    else:
        del arr[flag]


def insert(arr, n, capacity, item):
    # arr = array
    # n = length of array
    # capacity = max number of elements in array
    # item = element to be inserted in array
    if n > capacity:
        return n
    arr.append(None)
    i = n - 1
    while (i >= 0 and arr[i] > item):
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = item
    return n + 1

arr = [12, 23, 34, 45, 56]

item = 25
capacity = len(arr)
n = 5

print("Before Deletion")
print(arr)
delete(arr, 0)
print("After Deletion")
print(arr)

    
exit()


print("Before Insertion")
for i in arr:
    print(i, end = " ")
print()

insert(arr, n, capacity, item)

print("After Insertion")
for i in arr:
    print(i, end = " ")
    
