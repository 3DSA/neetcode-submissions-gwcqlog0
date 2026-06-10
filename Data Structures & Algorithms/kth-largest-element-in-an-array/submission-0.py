class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap of size k, and basically if it exceed size k we pop
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]