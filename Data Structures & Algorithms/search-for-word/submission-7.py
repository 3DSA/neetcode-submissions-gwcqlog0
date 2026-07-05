class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        def traverse(i, j, curr):
            nonlocal res
            if curr == len(word):
                res = True
                return
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[curr]:
                return
            temp = board[i][j]
            board[i][j] = "#"
            traverse(i+1, j, curr+1)
            traverse(i-1,j, curr+1)
            traverse(i, j+1, curr+1)
            traverse(i,j-1,curr+1)
            board[i][j] = temp
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    traverse(i, j, 0)
                    if res:
                        return res
        return False