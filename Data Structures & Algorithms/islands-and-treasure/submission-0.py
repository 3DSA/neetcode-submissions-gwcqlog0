class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # recursively go through 4 paths up down left right, out of bounds 
        def bfs(i, j,traversal):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or traversal > grid[i][j]:
                return
            grid[i][j] = min(grid[i][j], traversal)
            bfs(i+1, j, traversal+1)
            bfs(i-1, j, traversal+1)
            bfs(i, j+1, traversal+1)
            bfs(i, j-1, traversal+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j,0)


            
        
        