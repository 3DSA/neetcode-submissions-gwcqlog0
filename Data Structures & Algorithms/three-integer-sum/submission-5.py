class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        if not nums or len(nums) < 3:
            return res
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    right -=1
                    left +=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left +=1
        return list(res)