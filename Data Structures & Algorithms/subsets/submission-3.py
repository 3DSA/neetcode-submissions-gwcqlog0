class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def traverse(index, curr):
            if index == len(nums):
                res.add(tuple(curr.copy()))
                return
            curr.append(nums[index])
            traverse(index+1, curr)
            curr.pop()
            traverse(index+1, curr)
        
        traverse(0, [])
        sets = []
        for sub in res:
            sets.append(list(sub))
        return sets
        