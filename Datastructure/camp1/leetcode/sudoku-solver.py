class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = defaultdict(set)
        column = defaultdict(set)
        sub_box = defaultdict(set)


        sub_box_matrix = [[0,1,2],[3,4,5],[6,7,8]]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    box_id = r//3 * 3 + c // 3
                    val = int(val)
                    row[r].add(val)
                    column[c].add(val)
                    sub_box[box_id].add(val)

       
        def solve(i,j):
            nonlocal solved
            if i == 9:
                solved = True
                return
            
            nx_i = i + (j + 1)//9
            nx_j = (j + 1) % 9

            if board[i][j] != ".":
                solve(nx_i,nx_j)
            else:
                for cn in range(1,10):
                    box_id = i//3 * 3 + j // 3
                    if cn not in row[i] and cn not in column[j] and cn not in sub_box[box_id]:
                        board[i][j] = str(cn)
                        row[i].add(cn)
                        column[j].add(cn)
                        sub_box[box_id].add(cn)

                        solve(nx_i,nx_j)

                        if not solved:
                            board[i][j] = '.'
                            row[i].remove(cn)
                            column[j].remove(cn)
                            sub_box[box_id].remove(cn)
                

        solved = False
        solve(0,0)
