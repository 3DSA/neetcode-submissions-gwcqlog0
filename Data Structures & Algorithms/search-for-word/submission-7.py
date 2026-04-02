class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        indices = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    indices.append([i,j])
        
        res = False
        def search(i, word, row, col):
            nonlocal res
            if board[row][col] != word[i]:
                return
            i+=1
            temp = board[row][col]
            board[row][col] = "#"
            if i == len(word):
                res = True
                return
            if row-1 >= 0:
                search(i, word, row-1, col)
            if row+1 < len(board):
                search(i, word, row+1, col)
            if col-1 >= 0:
                search(i, word, row, col-1)
            if col+1 < len(board[0]):
                search(i, word, row, col+1)
            board[row][col] = temp
        for i in range(len(board)):
            for j in range(len(board[0])):
                search(0, word, i, j)
        return res 
            

            



        