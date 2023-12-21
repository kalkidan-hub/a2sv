class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        dell = 0
        # transpose, again
        m, n = len(strs), len(strs[0])

        for i in range(n):
            col = strs[0][i]
            for j in range(1,m):
                if col <= strs[j][i]:
                    col = strs[j][i]
                else:
                    dell += 1
                    break
        
        return dell
