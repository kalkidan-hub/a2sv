class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _sum = 0
        n = len(mat)

        for i in range(n):
            _sum += mat[i][i]
        for i,j in zip(range(n-1,-1,-1),range(n)):
            _sum += mat[i][j]

        return _sum - mat[n//2][n//2] if n&1 else _sum