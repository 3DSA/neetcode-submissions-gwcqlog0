class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = set()
        if not nums or len(nums) < 3:
            return triplets
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1   
                else:
                    k -=1
        
        return list(triplets)
        