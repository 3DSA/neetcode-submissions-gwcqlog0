class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search(i, j):
            nonlocal area
            if not (i>=0) or not (j>=0) or not (i<len(grid)) or not (j < len(grid[0])) or grid[i][j] != 1:
                return 0
            grid[i][j] = -1
            area +=1
            print(area)
            return search(i+1,j) + search(i,j+1) + search(i-1, j) + search(i,j-1)

        max_area = 0
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = 0
                if grid[i][j] == 1:
                    islands +=search(i,j)
                    max_area = max(max_area, area)
        return max_area