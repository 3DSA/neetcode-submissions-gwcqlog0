class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        arr = nums.copy()
        def dfs(curr, arr): # curr is current array, arr is nums copy
            nonlocal combinations
            if not arr:
                combinations.append(curr.copy())
                return
            
            for j in range(len(arr)):
                curr.append(arr.pop(j))
                dfs(curr, arr)
                arr.insert(j, curr.pop())

        dfs([], arr)
        return combinations
                

            


