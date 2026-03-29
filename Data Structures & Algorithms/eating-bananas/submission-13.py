import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minimum = None
        while l<=r:
            index = (r+l)//2
            total = 0
            for pile in piles:
                total += math.ceil(pile/index)
            if total <= h:
                if not minimum or index < minimum:
                    minimum = index
                r = index-1
            else:
                l = index+1
        return minimum
        