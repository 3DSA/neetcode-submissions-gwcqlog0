class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # keep a set for each row, col, and individual box
        # keeping track of row and col is easy, for the box we need a formula
        # lets make it easy, lets store the it into a map of tuples,'
        # tuple (0,0) represents top box
        cols = {}
        box = {}
        for i in range(len(board)):
            rows = set()
            for j in range(len(board[0])):
                if board[i][j] != ".":

                    cols.setdefault(j, set())
                    box.setdefault((i//3, j//3), set())
                    if board[i][j] in rows or board[i][j] in cols[j] or board[i][j] in box[(i//3, j//3)]:
                        return False
                    rows.add(board[i][j])
                    cols[j].add(board[i][j])
                    box[(i//3, j//3)].add(board[i][j])
        

        return True
        