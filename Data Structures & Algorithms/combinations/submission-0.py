class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def traverse(curr, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return
            if curr > n:
                return
            
            arr.append(curr)
            traverse(curr+1, arr)
            arr.pop()
            traverse(curr+1, arr)

        traverse(1, [])
        return res
        