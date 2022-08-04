class Solution:
    def rob(self, nums: List[int]) -> int:
        ### https://leetcode.com/problems/house-robber/
        @lru_cache(None)
        def solve(idx):
            if idx >= n:
                return 0

            return max(solve(idx + 1), solve(idx + 2) + nums[idx])

        return solve(0)