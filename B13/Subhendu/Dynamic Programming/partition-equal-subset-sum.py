class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ### https://leetcode.com/problems/partition-equal-subset-sum/
        tsum = sum(nums)
        if tsum % 2 == 1:
            return False

        memo = {}

        def solve(idx, target):
            if target == 0:
                return True

            if idx >= len(nums):
                return False
            if (idx, target) in memo:
                return memo[(idx, target)]

            incl = False
            if nums[idx] <= target:
                incl = solve(idx + 1, target - nums[idx])
            exclu = solve(idx + 1, target)

            memo[(idx, target)] = incl or exclu
            return incl or exclu

        return solve(0, tsum // 2)