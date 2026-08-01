class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        total = 1
        for num in nums:
            res.append(total)
            total*= num
        
        total = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= total
            total *= nums[i]
        return res
        

        