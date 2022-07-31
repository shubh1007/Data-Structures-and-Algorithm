class Sort:
    def insertionSort(self, arr):
        left, right = 0,1
        for left in range(len(arr)):
            minVal = arr[left]
            for right in range(left + 1, len(arr)):
                if arr[right] < minVal:
                    arr[right], arr[left] = arr[left], arr[right]
        return arr

    def bubbleSort(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    def quickSort(self, arr, low, high):
        def partition(arr, low, high):
            pivot = arr[low]
            count = 0
            for i in range(low + 1, high + 1):
                if arr[i] <= pivot: count += 1
            pivotIdx = count + low
            arr[pivotIdx], arr[low] = arr[low], arr[pivotIdx]
            i, j = low, high
            while i < pivotIdx and j > pivotIdx:
                while arr[i] < pivot: i += 1
                while arr[j] > pivot: j -= 1
                if i < pivotIdx and j > pivotIdx:
                    arr[i], arr[j] = arr[j], arr[i]
            return pivotIdx
            
            
        if low < high:
            pidx = partition(arr, low, high)
            self.quickSort(arr, low, pidx - 1)
            self.quickSort(arr, pidx + 1, high)

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            
            self.mergeSort(left)
            self.mergeSort(right)

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
            
            

arr = [5, 4, 4, 3, 2, 1, 1]
sol = Sort()

print(f"Before sorting : {arr}")
result = sol.mergeSort(arr)
print(f"After sorting : {arr}")
            
