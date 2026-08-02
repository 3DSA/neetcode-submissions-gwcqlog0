class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[k] + nums[j] == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[k] + nums[j] < 0:
                    j += 1
                else:
                    k -=1
        
        result = []
        for group in res:
            result.append(list(group))
        return result

        