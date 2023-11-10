class Solution:
    def topKFrequent(self, words, k):
        #To Return : results
        results = []
        count = {}
        for word in words:
            # count the number of times the words are repeated int the list.
            count[word] = count.get(word, 0) + 1
        # Initiate the heap 
        heap = []
        for key, value in count.items():
            # Push the count of words one by one in the max-heap
            heapq.heappush(heap, (-value, key))        
        
        for i in range(k):
            # Now append the k most frequent words used by popping elements from heap
            results.append(heapq.heappop(heap)[1])    
        # return results list containing k elements which are those k frequent words 
        return results
    
  

    
