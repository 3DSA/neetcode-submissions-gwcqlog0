class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(-stone)
        heapq.heapify(heap)
        def smash():
            if len(heap) == 1:
                return - heapq.heappop(heap)
            if len(heap) == 0:
                return 0
            remainder = heapq.heappop(heap) - heapq.heappop(heap)
            if remainder != 0:
                heapq.heappush(heap, remainder)
            return smash()
        return smash()   
        