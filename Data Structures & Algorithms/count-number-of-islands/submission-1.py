class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # traverse through grid, and change vals to #
        def traverse(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >=len(grid[0]) or grid[i][j] != "1":
                return
            grid[i][j] = "#"
            traverse(i+1, j)
            traverse(i-1, j)
            traverse(i, j+1)
            traverse(i, j-1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    traverse(i, j)
        return count
        