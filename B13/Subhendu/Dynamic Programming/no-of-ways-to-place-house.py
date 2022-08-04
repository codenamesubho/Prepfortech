class Solution:
    def countHousePlacements(self, n: int) -> int:
        ### https://leetcode.com/problems/count-number-of-ways-to-place-houses/
        @lru_cache(None)
        def solve(idx, is_filled):
            if idx == 1:
                return 1
            if is_filled:
                return solve(idx - 1, not is_filled)  # % (1000000000 + 7)
            else:
                return (solve(idx - 1, is_filled) + solve(idx - 1, not is_filled))  # % ((1000000000 + 7))

        r = solve(n, True) + solve(n, False)
        return int(r ** 2 % (1000000000 + 7))