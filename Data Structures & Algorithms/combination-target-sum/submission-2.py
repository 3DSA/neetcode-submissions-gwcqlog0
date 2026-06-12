class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        def sums(index, curr, arr):
            if curr == target:
                res.add(tuple(arr.copy()))
                return
            if index == len(nums) or curr > target:
                return
            
            arr.append(nums[index])
            sums(index, curr+nums[index], arr)
            arr.pop()
            sums(index+1, curr, arr)
        
        sums(0, 0, [])
        combinations = []
        for sub in res:
            combinations.append(list(sub))
        return combinations
