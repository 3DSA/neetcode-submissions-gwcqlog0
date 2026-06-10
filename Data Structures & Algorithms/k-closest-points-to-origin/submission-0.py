class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            distance = ((point[0]-0)**2 + (point[1]-0) ** 2) ** 1/2
            heapq.heappush(heap, [distance, point])
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res
        
        