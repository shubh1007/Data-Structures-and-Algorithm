import sys


def subArraySum(arr, SUM):
    N = len(arr)
    left, right = 0, 0
    csum = arr[0]
    while right < N and left >= 0:
        csum += arr[right]
        if csum == SUM:
            return [left, right]
        elif csum > SUM:
            csum -= arr[left]
            left += 1
        else:
            right += 1
            
        



    
arr = [1,2,3,7,5]
result = subArraySum(arr, 12)
print(result)
            
        
    
        


















def kadaneAlgo(arr):
    maxVal = -sys.maxsize - 1
    N = len(arr)
    SUM = 0
    for i in range(N):
        SUM += arr[i]
        maxVal = max(maxVal, SUM)
        if SUM < 0:
            SUM = 0
    return maxVal

"""
arr= [-1, -2, -3, -4, -5]
result = kadaneAlgo(arr)
print(result)
""" 
    
    



































"https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1"
