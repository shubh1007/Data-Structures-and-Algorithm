# NOT SOLVED FOR NEGATIVE INPUT VALUES

import heapq

class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        if abs(len(self.minHeap) - len(self.maxHeap)) >= 2: 
            temp = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, temp)

    def findMedian(self) -> float:
        temp = 0
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            min_temp = heapq.heappop(self.minHeap)
            max_temp = heapq.heappop(self.maxHeap)
            temp = ( min_temp - max_temp) / 2.0
            heapq.heappush(self.maxHeap, max_temp)
            heapq.heappush(self.minHeap, min_temp)
        else:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, temp)
        return temp
        












# from heapq import heappush, heappop, heappushpop

# class MedianFinder:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.upperHeap = [float('inf')]
#         self.lowerHeap = [float('inf')]
#         # lowerHeap's numbers are minus original numbers, because in Python heap is min-heap

#         # always maintain that their lens are equal, or upper has 1 more than lower

#     def addNum(self, num):
#         """
#         Adds a num into the data structure.
#         :type num: int
#         :rtype: void
#         """
#         upperMin = + self.upperHeap[0]
#         lowerMax = - self.lowerHeap[0]

#         if num > upperMin or (lowerMax<=num<=upperMin and len(self.upperHeap)==len(self.lowerHeap)):
#             heappush(self.upperHeap, num)
#         else:
#             heappush(self.lowerHeap, -num)

#         # maintain the invariant that their lens are equal, or upper has 1 more than lower
#         if len(self.upperHeap)-len(self.lowerHeap) > 1:
#             heappush( self.lowerHeap, -heappop( self.upperHeap ) )
#         elif len(self.lowerHeap) > len(self.upperHeap):
#             heappush( self.upperHeap, -heappop( self.lowerHeap ) )


#     def findMedian(self):
#         """
#         Returns the median of current data stream
#         :rtype: float
#         """
#         if len(self.upperHeap) == len(self.lowerHeap):
#             upperMin = + self.upperHeap[0]
#             lowerMax = - self.lowerHeap[0]
#             return ( float(upperMin) + float(lowerMax) ) / 2.0
#         else:
#             assert len(self.upperHeap) == len(self.lowerHeap) + 1
#             return float(self.upperHeap[0])

