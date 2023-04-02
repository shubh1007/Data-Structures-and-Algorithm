from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = [0 for i in range(len(spells))]
        def helper(spell):
            l = 0
            r = len(potions)   
            while l < r:
                mid = (l + r) // 2
                if potions[mid] * spell >= success:
                    r = mid
                else:
                    l = mid + 1
            return l 
        return [len(potions) - helper(spell) for spell in spells]
        
 