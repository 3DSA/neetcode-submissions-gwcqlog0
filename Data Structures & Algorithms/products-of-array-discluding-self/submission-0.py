class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod =[1] * len(nums)
        left = 1
        for i in range(len(nums)):
            prod[i] = left
            left *= nums[i]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            prod[i] *= right
            right *= nums[i]
        return prod
            


        