class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def bfs(i, curr):
            if i == len(nums):
                res.add(tuple(curr.copy()))
                return
            
            curr.append(nums[i])
            bfs(i+1, curr)
            curr.pop()
            bfs(i+1, curr)

        
        groups = []
        bfs(0, [])
        for group in res:
            groups.append(list(group))
        return groups
        