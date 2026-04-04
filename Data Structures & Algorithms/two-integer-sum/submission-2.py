class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            maps[target-nums[i]] = i
        

        for i in range(len(nums)):
            if nums[i] in maps and i != maps[nums[i]]:
                return sorted([i, maps[nums[i]]])
        return -1




        