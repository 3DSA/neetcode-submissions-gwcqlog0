class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        box = {}
        for i in range(9):
            cols[i] = set()
            box[i] = set() 
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                box_compute = 3*(i//3) + (j//3)
                if board[i][j] != ".":
                    if board[i][j] in row or board[i][j] in cols[j] or  board[i][j] in box[box_compute]:
                        return False
                    row.add(board[i][j])
                    cols[j].add(board[i][j])
                    box[box_compute].add(board[i][j])
        return True