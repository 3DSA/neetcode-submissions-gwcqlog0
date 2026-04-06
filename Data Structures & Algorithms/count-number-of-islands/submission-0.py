class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        def search(i, j):
            if not (i>=0) or not (j>=0) or not (i<len(grid)) or not (j < len(grid[0])) or grid[i][j] != "1":
                return 0
            grid[i][j] = "#"
            return search(i+1,j) + search(i,j+1) + search(i-1, j) + search(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands +=1 + search(i,j)
        return islands



        