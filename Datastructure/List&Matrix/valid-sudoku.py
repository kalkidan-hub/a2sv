class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            s_row = set()
            s_column = set()

            # check all rows
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in s_row:
                        return False
                    else:
                        s_row.add(board[i][j])

                # check all column, 
                if board[j][i] != ".":
                    if board[j][i] in s_column:
                        return False
                    else:
                        s_column.add(board[j][i])
        
        # check the nine 3 X 3
        for i in range(1,9,3):
            for j in range(1,9,3):
                s_block = set()
                surr = [(i-1,j),(i-1,j-1),(i-1,j+1),(i,j),(i,j-1),(i,j+1),(i+1,j),(i+1,j-1),(i+1,j+1)]
                for x,y in surr:
                    if board[x][y] != ".":
                        if board[x][y] in s_block:
                            return False
                        else:
                            s_block.add(board[x][y])
        return True
