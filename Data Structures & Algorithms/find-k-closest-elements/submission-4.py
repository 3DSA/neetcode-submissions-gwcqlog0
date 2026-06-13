class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use a min heap, for this
        # we can start window off at max, l = 0, and right index
        # until window is as small as k
        l = 0
        r = len(arr)-1
        while r-l+1 != k:
            if abs(arr[l]-x) > abs(arr[r]-x):
                l += 1
            else:
                r-=1
        return arr[l:r+1]
        