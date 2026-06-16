import heapq
class Solution:
    def getMedian(self, arr):
        # code here
        max_heap = []
        min_heap = []
        result = []
        
        for num in arr:
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            if len(max_heap) > len(min_heap):
                result.append(float(-max_heap[0]))
            else:
                result.append((-max_heap[0] + min_heap[0]) / 2.0)
        return result