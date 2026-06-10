class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        l = 0
        curr = set()
        for r in range(len(nums)):
            if r-l > k:
                curr.remove(nums[l])
                l+=1
            if nums[r] in curr:
                return True
            curr.add(nums[r])

        return False
        