class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        ### https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
        @lru_cache(None)
        def rec(d, tgt, k):
            if d == 0 and tgt == 0:
                return 1

            if d == 0 or tgt == 0:
                return 0

            ans = 0

            for i in range(k):
                ans += rec(d - 1, tgt - i, k)
            return ans % 1000000007

        return rec(n, target, k)