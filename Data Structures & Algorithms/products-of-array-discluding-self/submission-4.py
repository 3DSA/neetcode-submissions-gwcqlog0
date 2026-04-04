class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        total = 1
        for num in nums:
            arr.append(total)
            total *= num
        
        total = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] *= total
            total *= nums[i]
        return arr
        