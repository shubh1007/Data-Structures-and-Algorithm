class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def isPossible(i):
            if ((i - 1 >=0 and flowerbed[i-1]==1) or (i + 1 < len(flowerbed) and flowerbed[i+1]==1)):
                return False
            return True
            
        if n == 0: return True
        count = 0
        for index in range(len(flowerbed)):
            if flowerbed[index] == 0 and isPossible(index):
                flowerbed[index] = 1
                count += 1
            if count == n:
                return True
        return False





