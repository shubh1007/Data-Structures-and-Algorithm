class Solution:
    def topKFrequent(self, words, k):
        results = []
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))        
        for i in range(k):
            results.append(heapq.heappop(heap)[1])
        
        return results
