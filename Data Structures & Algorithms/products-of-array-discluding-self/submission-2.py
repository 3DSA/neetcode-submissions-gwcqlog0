class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [1] * len(nums)
        total = 1
        for i in range(0, len(nums)): #prefix
            if not prefix:
                prefix.append(total)
            else:
                total *=nums[i-1]
                prefix.append(total)
        total = 1
        for i in range(len(nums)-1, -1, -1): #suffix
            suffix[i] = total
            total *=nums[i]
        print(suffix)
        res = []
        for i in range(0, len(nums)):
            res.append(suffix[i]*prefix[i])
        return res
        



        