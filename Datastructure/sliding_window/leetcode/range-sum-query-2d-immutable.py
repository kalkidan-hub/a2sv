class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m = len(matrix),len(matrix[0])
        self.prf_sum = [[0] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0:
                    self.prf_sum[i].append(self.prf_sum[i][-1] + matrix[i][j])
                else:
                    self.prf_sum[i].append(self.prf_sum[i][-1] + self.prf_sum[i-1][j + 1] - self.prf_sum[i-1][j] + matrix[i][j])

        
        self.prf_sum = [[0 for _ in range(m+1)]] + self.prf_sum
        print(self.prf_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        col1 += 1
        col2 += 1
        row1 += 1
        row2 += 1

        return self.prf_sum[row2][col2] - self.prf_sum[row2][col1-1] - self.prf_sum[row1-1][col2] + self.prf_sum[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)