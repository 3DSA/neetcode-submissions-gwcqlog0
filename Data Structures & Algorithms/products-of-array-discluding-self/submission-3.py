class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        total = 1
        for i in range(len(nums)):
            products.append(total)
            total *= nums[i]
        total = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= total
            total *= nums[i]
        return products
        
