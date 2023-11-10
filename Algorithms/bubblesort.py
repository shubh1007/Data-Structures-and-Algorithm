def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        MergeSort(left)
        MergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1




def MERGE(arr, left, mid, right):
    i = j = k = 0
    LEFT = arr[left: mid]
    RIGHT = arr[mid: right + 1]
    while i < len(LEFT) and j < len(RIGHT):
        if LEFT[i] < RIGHT[j]:
            arr[k] = LEFT[i]
            i += 1
        else:
            arr[k] = RIGHT[j]
            j += 1
        k += 1
    while i < len(LEFT):
        arr[k] = LEFT[i]
        i += 1
        k += 1
    while j < len(RIGHT):
        arr[k] = RIGHT[j]
        j += 1
        k += 1


def MERGESORT(arr, left, right):
    print(left)
    if left >= right:
        return
    else:
        mid = (right - left) // 2
        MERGESORT(arr, left, mid)
        MERGESORT(arr, mid + 1, right)
        MERGE(arr, left, mid, right)


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

a = [4, 3, 2, 1, 1]
# print(bubbleSort(a))
# MERGESORT(a, 0, len(a) - 1)
MergeSort(a)
print(a)