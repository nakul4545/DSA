import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # the question is of closest means use maxheap 
        x = [[-sqrt((i[0]-0)**2 + (i[1] - 0) **2), i] for i in points]
        # x = [[-(i[0]**2 + i[1]**2),i] for i in points] 
        #Instead of storing sqrt we can store squared distance
        # Store sqrt along with i because at the end you're returning i not sqrt
        heap = x[:k]
        heapq.heapify(heap)
        for i in x[k:]:
            if i[0] > heap[0][0]:
                heapq.heapreplace(heap,i)
        return [num for sqrrt, num in heap]

        