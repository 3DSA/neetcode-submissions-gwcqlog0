class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        def dfs(i, curr, total, target):
            if total == target:
                combinations.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i], target)
            curr.pop()
            dfs(i+1, curr, total, target)
        dfs(0, [], 0, target)
        return combinations

           
                