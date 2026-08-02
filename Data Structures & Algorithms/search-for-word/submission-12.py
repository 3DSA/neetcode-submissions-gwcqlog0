class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cond = False
        def bfs(i,j, curr):
            nonlocal word
            nonlocal cond
            if curr == len(word):
                cond = True
                return
            if i < 0 or i >= len(board) or j < 0 or j >= (len(board[0])) or board[i][j] != word[curr]:
                return
            
            temp = board[i][j]
            board[i][j] = "#"
            bfs(i+1,j, curr+1)
            bfs(i-1,j, curr+1)
            bfs(i,j+1, curr+1)
            bfs(i,j-1, curr+1)
            board[i][j] = temp

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                bfs(i,j, 0)
                if cond:
                    return True
        return False
        