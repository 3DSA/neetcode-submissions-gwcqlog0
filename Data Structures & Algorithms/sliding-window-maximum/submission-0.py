class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        # have a heap, gives us current max o(1), o logn(n) to add
        # have 2d array in heap [val, index] and if index > left we pop index
        l = 0
        res = []
        for r in range(len(nums)):
            heapq.heappush(heap, [-nums[r], r])
            if r-l+1 == k:
                while heap[0][1] < l:
                    heapq.heappop(heap)
                res.append(- heap[0][0])
                l += 1
        return res
            
                
