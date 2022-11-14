class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
    
        rowTable, colTable = defaultdict(set), defaultdict(set)
        
        for i, (row, col) in enumerate(stones):
            rowTable[row].add(i)
            colTable[col].add(i)
        
        graph = defaultdict(set)
        for i, (row, col) in enumerate(stones): 
            graph[i] = rowTable[row].union(colTable[col])
            graph[i].remove(i)
            
        visited = set()
                
        def dfs(stone_idx):
            nonlocal graph, visited
            if stone_idx in visited:
                return
            
            visited.add(stone_idx)
            for next_stone in graph[stone_idx]:
                if next_stone not in visited:
                    dfs(next_stone)
        
        stone_left = 0
        print(graph)
        for stone_idx in range(len(stones)):
            if stone_idx not in visited:
                dfs(stone_idx)
                stone_left += 1
        return len(stones) - stone_left
        
