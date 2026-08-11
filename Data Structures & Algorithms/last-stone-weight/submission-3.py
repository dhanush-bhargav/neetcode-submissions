import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones_heap = [-s for s in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            y = heapq.heappop(stones_heap)
            x = heapq.heappop(stones_heap)
            if x > y :
                heapq.heappush(stones_heap, y-x)
        if len(stones_heap) == 0:
            return 0
        else:
            return abs(stones_heap[0])