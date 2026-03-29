class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            mid = (l+r) // 2
            print(nums[mid])
            if nums[mid] == target:
                    return mid
            elif nums[l] < nums[r]:
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            else: #when left index is greater than right
                if nums[l] <= nums[mid]:
                    if nums[mid] < target or nums[l] > target:
                        l = mid+1
                    else:
                        r = mid-1
                else: # l > mid
                    if target < nums[mid] or target > nums[r]:
                        r = mid -1
                    else:
                        l = mid+1
                
                
        
        return -1
        