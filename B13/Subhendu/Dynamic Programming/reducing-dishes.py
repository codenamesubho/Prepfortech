class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        ### https://leetcode.com/problems/reducing-dishes/
        sat.sort()

        memo = {}

        def solve(idx, t):
            if idx >= len(sat):
                return 0

            inclu = t * sat[idx] + solve(idx + 1, t + 1)
            exclu = solve(idx + 1, t)
            return max(inclu, exclu)

        return solve(0, 1)