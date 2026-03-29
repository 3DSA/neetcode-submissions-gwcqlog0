class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(0,len(nums)):
            #. target - number = index
            maps[target - nums[i]] = i
        for i in range(0,len(nums)):
            if nums[i] in maps:
                if i != maps[nums[i]]:
                    return [i, maps[nums[i]]]


        