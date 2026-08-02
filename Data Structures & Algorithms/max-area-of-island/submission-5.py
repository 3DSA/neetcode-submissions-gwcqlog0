class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            res = 1 + bfs(i+1, j) + bfs(i-1,j) + bfs(i,j-1) + bfs(i,j+1)
            return res
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, bfs(i,j))
        return area
        