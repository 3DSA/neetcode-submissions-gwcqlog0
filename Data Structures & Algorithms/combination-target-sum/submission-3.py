class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        def dfs(i, total, arr): #index, total of arr, arr
            if total == target:
                res.add(tuple(arr.copy()))
                return
            if i == len(nums) or total > target:
                return

            arr.append(nums[i])
            dfs(i, total+nums[i], arr)
            arr.pop()
            dfs(i+1, total, arr)
        
        dfs(0, 0, [])

        new = []
        for group in res:
            new.append(list(group))
        return new
        