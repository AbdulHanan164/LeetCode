class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for i in range(1, n):
            min_val = min(grid[i - 1])
            min_second_val = min(
                grid[i - 1][:grid[i - 1].index(min_val)] + grid[i - 1][grid[i - 1].index(min_val) + 1:])
            for j in range(n):
                if grid[i - 1][j] == min_val:
                    grid[i][j] += min_second_val
                else:
                    grid[i][j] += min_val

        return min(grid[-1])
