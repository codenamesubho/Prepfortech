class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ### https://leetcode.com/problems/target-sum/

        @lru_cache(None)
        def solve(idx, s):
            if idx == len(nums):
                if s == target:
                    return 1
                else:
                    return 0

            if idx > len(nums) - 1:
                return 0

            return solve(idx + 1, s + nums[idx]) + solve(idx + 1, s - nums[idx])

        return solve(0, 0)