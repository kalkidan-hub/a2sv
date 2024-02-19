class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = []
        for j in range(len(grid[0])):
            mx = -1
            for i in range(len(grid)):
                mx = max(mx,grid[i][j])
            col_max.append(mx)

        grid_new_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid_new_sum += min(row_max[i],col_max[j]) - grid[i][j]

        return grid_new_sum