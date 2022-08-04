class Solution:
    def climbStairs(self, n: int) -> int:
        ### https://leetcode.com/problems/climbing-stairs/
        def solve(k):
            if k > n:
                return 0
            if k == n:
                return 1

            return solve(k + 1) + solve(k + 2)

        return solve(0)