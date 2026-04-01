class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        arr = nums.copy()
        def dfs(i, curr, arr): # curr is current array, arr is nums copy
            nonlocal combinations
            if i == len(nums):
                combinations.append(curr.copy())
                return
            
            for j in range(len(arr)):
                curr.append(arr.pop(j))
                dfs(i+1, curr, arr)
                arr.insert(j, curr.pop())

        dfs(0, [], arr)
        return combinations
                

            


