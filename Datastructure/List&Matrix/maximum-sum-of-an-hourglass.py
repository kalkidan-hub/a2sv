class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0

        for i in range(len(grid) - 2):
            for j in range(1,len(grid[0])-1):
                hour_sum = grid[i][j] + grid[i][j-1] + grid[i][j+1]+ grid[i+1][j] + grid[i+2][j] + grid[i+2][j-1] + grid[i+2][j+1]
                max_sum = max(max_sum,hour_sum)

        return max_sum