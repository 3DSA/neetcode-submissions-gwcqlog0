class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # os connected to edge of board cannot be touched
        # find the os on edge of board, mark them,
        # for those regions surrounded, replace them
        # lets hold a set the cant replace os
        # iterate through row 0 column 0, row 0 columm -1, row
    
        regions = set()

        def find(i,j):
            if (i,j) in regions or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O":
                return
            # this means its a addition not discovered yet connected to region
            regions.add((i,j))
            find(i+1,j)
            find(i-1,j)
            find(i,j+1)
            find(i,j-1)
            
        rows = [0, len(board)-1]
        cols = [0, len(board[0])-1]
        for i in rows:
            for j in range(len(board[0])):
                find(i,j)
        for i in range(len(board)):
            for j in cols:
                find(i,j)
        print(regions)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if (i,j) not in regions:
                        board[i][j] = "X"



        