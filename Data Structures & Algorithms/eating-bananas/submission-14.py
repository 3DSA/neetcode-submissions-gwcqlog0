class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_rate = r
        while l <= r:
            rate = (l+r) // 2
            hours = 0
            for i in piles:
                hours += -(-i // rate)
            if hours > h:
                l = rate + 1
            else:
                r = rate - 1
                min_rate = min(min_rate, rate)
        return min_rate
        