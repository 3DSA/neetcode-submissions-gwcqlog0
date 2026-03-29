class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set(nums)
        if len(dupes) < len(nums):
            return True
        return False
         