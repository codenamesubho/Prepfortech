class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def solve(stair):
            ### https://leetcode.com/problems/min-cost-climbing-stairs/
            if stair <= 1:
                return 0
            one = cost[stair-1] + solve(stair-1)
            two = cost[stair-2] + solve(stair-2)
            return min(one,two)

        return solve(len(cost))
