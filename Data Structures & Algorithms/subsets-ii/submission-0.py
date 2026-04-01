class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        combinations = set()
        nums.sort()
        def dfs(i, curr):
            if i == len(nums):
                combinations.add(tuple(curr.copy()))
                return
            
            
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        dfs(0, [])
        res = []
        for sub in combinations:
            res.append(list(sub))
        return res
            
        