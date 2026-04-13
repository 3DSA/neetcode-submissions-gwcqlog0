class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        groups = set()
        nums.sort()
        def traverse(i, curr):
            if i > len(nums)-1:
                groups.add(tuple(curr))
                return
            
            curr.append(nums[i])
            traverse(i+1, curr)
            curr.pop()
            traverse(i+1, curr)
        traverse(0, [])
        res = []
        for group in groups:
            res.append(list(group))
        return res
        