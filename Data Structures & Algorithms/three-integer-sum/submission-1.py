class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = set()
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    arr.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[j] + nums[k] + nums[i] < 0:
                    j+=1
                else:
                    k-=1
        return [list(sols) for sols in arr ]
                
        