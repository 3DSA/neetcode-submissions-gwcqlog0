class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 # left pointer
        curr = 0 # current total 
        size = float('inf')
        for r in range(len(nums)):
            curr += nums[r]
            while curr - nums[l] >= target:
                print(r)
                curr -= nums[l]
                l += 1
            if curr >= target:
                size = min(size, r-l+1)

        if size == float('inf'):
            return 0
        return size
            
