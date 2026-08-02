class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        res = 0 # count of subarrays
        l = 0
        for r in range(len(arr)):
            total += arr[r]
            if r-l+1 > k:
                total -= arr[l]
                print(f"total:{total} num:{arr[r]}")
                l+=1
            if r-l+1 == k and total >= threshold*k:
                res += 1
        return res
            

        