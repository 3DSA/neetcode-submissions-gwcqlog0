class Solution:
    def bfs(self, nums):
        queue = []
        arr = [[]]
        for i in nums:
            new_list = [sublist + [i] for sublist in arr]
            arr.extend(new_list)
        return arr


            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.bfs(nums)
        
        