class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        myHash = {}
        for i in arr:
            if i not in myHash:
                myHash[i] = 1
            else:
                myHash[i] += 1
        values = list(myHash.values())
        values.sort()
        for i in range(len(values)-1):
            if values[i] == values[i+1]:
                return False
        return True
            
