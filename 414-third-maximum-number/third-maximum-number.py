import heapq
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        heap = [-i for i in set(nums)]
        heapq.heapify(heap)
        for _ in range(2):
            heapq.heappop(heap)
        return -heapq.heappop(heap)