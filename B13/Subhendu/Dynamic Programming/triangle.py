class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def helper():
            if i == n - 1:
                return triangle[i][j]

            bottom = triangle[i][j] + helper(i + 1, j)
            bottom_down = triangle[i][j] + helper(i + 1, j + 1)

            return max(bottom, bottom_down)
