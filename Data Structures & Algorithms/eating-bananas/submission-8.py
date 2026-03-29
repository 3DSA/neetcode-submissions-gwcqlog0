class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lbound = 1
        rbound = max(piles)
        if len(piles) == h:
            return rbound
        while lbound < rbound:
            hours = 0
            mid = (lbound+rbound) // 2
            print(mid)
            for i in piles:
                res = (i + mid - 1) // mid
                hours += res
            if hours <= h:
               rbound = mid
            else:
                lbound = mid+1
            # print(lbound)
            # print(rbound)
        return lbound




        