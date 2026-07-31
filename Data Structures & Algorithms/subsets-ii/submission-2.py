class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def subsets(i, curr):
            if i == len(nums):
                res.add(tuple(curr.copy()))
                return
            curr.append(nums[i])
            subsets(i+1, curr)
            curr.pop()
            subsets(i+1, curr)
        subsets(0, [])
        groups = []
        for group in res:
            groups.append(list(group))
        return groups
        