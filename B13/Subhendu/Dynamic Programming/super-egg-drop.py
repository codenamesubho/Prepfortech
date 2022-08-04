class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        ### https://leetcode.com/problems/super-egg-drop/
        @lru_cache(None)
        def help(K, N):
            if N <= 1:
                return N

            if K == 1:
                return N

            ans = 0
            mn = float('inf')
            for i in range(1, N + 1):
                ans = 1 + max(help(K - 1, i - 1), help(K, N - i))

                mn = min(mn, ans)
            return mn

        return help(k, n)