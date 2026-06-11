class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_rate = r
        while l<=r:
            mid = (l+r) // 2
            hours = 0
            for pile in piles:
                hours += -(-pile//mid)
            if hours <= h:
                min_rate = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_rate
        