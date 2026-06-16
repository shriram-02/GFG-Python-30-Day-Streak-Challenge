import heapq
class Solution:
    def mergeArrays(self, mat):
        # Code here
        heap = []
        result = []
        
        for i in range(len(mat)):
            heapq.heappush(heap,(mat[i][0],i,0))
        while heap:
            val , r , c = heapq.heappop(heap)
            result.append(val)
            
            if c + 1 < len(mat[r]):
                heapq.heappush(heap,(mat[r][c + 1],r,c + 1))
        return result