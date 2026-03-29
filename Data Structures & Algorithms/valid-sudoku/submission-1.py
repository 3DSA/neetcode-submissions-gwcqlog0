class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        quads = {
            0: set([]),
            1: set([]),
            2: set([]),
            3: set([]),
            4: set([]),
            5: set([]),
            6: set([]),
            7: set([]),
            8: set([])
        }
        cols = {
            0: set([]),
            1: set([]),
            2: set([]),
            3: set([]),
            4: set([]),
            5: set([]),
            6: set([]),
            7: set([]),
            8: set([])
        }
        for i in range(9):
            row = set([])
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in row: # check for row
                        row.add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in cols[j]: # check for col
                        cols[j].add(board[i][j])
                    else:
                        return False
                    quads_index = (i//3)*3 + (j//3)
                    if board[i][j] not in quads[quads_index]: # check for quad
                        quads[quads_index].add(board[i][j])
                    else:
                        return False
        return True
                