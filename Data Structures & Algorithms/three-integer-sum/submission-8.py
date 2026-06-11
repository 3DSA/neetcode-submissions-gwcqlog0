class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -=1
        arr = []
        for sub in res:
            arr.append(list(sub))
        return arr