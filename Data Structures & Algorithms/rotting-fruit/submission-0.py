class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    fruit += 1
                if grid[i][j] == 2:
                    queue.append([i,j,0])
        
        def check(i,j,curr):
            if i < 0 or j < 0 or i >=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            queue.append([i,j,curr])
        
        time = 0
        print(fruit)
        while queue:
            i,j, curr = queue.popleft()
            time = curr
            fruit -= 1
            check(i-1,j,curr+1)
            check(i+1,j,curr+1)
            check(i,j-1,curr+1)
            check(i,j+1,curr+1)

        print(fruit)
        if fruit != 0:
            return -1
        return time

        