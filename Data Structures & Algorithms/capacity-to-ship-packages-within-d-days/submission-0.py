class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        min_weight = r
        while l <= r:
            mid = (l+r)//2
            count = 0
            remainder = 0
            for weight in weights:
                if remainder >= weight:
                    remainder -= weight
                else:
                    remainder = mid - weight
                    count += 1
            if count <= days:
                min_weight = min(min_weight, mid)
                r = mid-1
            else:
                l = mid+1
        return min_weight


        