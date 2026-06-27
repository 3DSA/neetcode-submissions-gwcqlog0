class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def traverse(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0

            return 1 + traverse(i-1, j) + traverse(i+1, j) + traverse(i, j-1) + traverse(i, j+1)

        
        area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, traverse(i,j))
        return area
        