class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
       
        m,n = len(matrix),len(matrix[0])
        trans_matrix = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                trans_matrix[i][j] = matrix[j][i]

        return trans_matrix