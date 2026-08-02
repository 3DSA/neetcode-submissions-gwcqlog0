class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def traverse(i,j,curr):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or curr > grid[i][j]:
                return
            grid[i][j] = curr
            traverse(i-1,j,curr+1)
            traverse(i+1,j,curr+1)
            traverse(i,j-1,curr+1)
            traverse(i,j+1,curr+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    traverse(i,j,0)
        