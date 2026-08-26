from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums) 
        x = [[count, num] for num, count in cnt.items()]
        heap = x[:k]
        heapq.heapify(heap)
        for i in x[k:]:
            if i[0] > heap[0][0]:
                heapq.heapreplace(heap,i)
        return [num for count , num in heap]
       