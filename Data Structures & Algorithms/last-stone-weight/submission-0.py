import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-s for s in stones] #nax heap
        heapq.heapify(stone_heap)

        while not len(stone_heap) <= 1:
            y = -heapq.heappop(stone_heap)
            x = -heapq.heappop(stone_heap)

            if y != x:
                heapq.heappush(stone_heap, -(y - x))

        if len(stone_heap) == 1:
            return abs(stone_heap.pop())
        else:
            return 0


