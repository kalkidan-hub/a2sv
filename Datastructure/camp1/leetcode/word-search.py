class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m,n = len(board), len(board[0])

        def backtrack(i,j,idx,trace):
            nonlocal m,n
            if idx == len(word):
                return True
            
            candidates = [(i + 1,j),(i,j + 1),(i - 1,j),(i, j - 1)]
            for nxi,nxj in candidates:
                if 0 <= nxi < m and 0 <= nxj < n and (nxi,nxj) not in trace:
                    if board[nxi][nxj] == word[idx]:
                        trace.add((nxi,nxj))
                        if backtrack(nxi,nxj,idx + 1, trace):
                            return True
                        trace.remove((nxi,nxj))
        ans = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    ans = ans or backtrack(i,j,1,{(i,j)})
        
        return ans