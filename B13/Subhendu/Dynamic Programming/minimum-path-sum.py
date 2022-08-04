class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ### https://leetcode.com/problems/minimum-path-sum/
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * (n) for _ in range(m)]

        for i in range(0, m, 1):
            for j in range(0, n, 1):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])

        return dp[m - 1][n - 1]