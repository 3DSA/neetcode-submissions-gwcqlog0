class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            nonlocal area
            if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] != 1:
                return
            area += 1
            print(area)
            grid[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = 0
                dfs(i,j)
                max_area = max(max_area, area)
        return max_area


        

        
        