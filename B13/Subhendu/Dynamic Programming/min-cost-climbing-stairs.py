class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ### https://leetcode.com/problems/min-cost-climbing-stairs/
        @lru_cache(None)
        def solve(stair):
            if stair == len(cost):
                return 0
            if stair > len(cost):
                return float('inf')

            one = cost[stair] + solve(stair + 1)
            two = cost[stair] + solve(stair + 2)
            return min(one, two)

        return min(solve(0), solve(1))