class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ### https://leetcode.com/problems/interleaving-string/
        memo = {}
        if len(s3) != len(s1) + len(s2):
            return False

        def solve(p1, p2, p3):
            if p3 == len(s3):
                if p1 == len(s1) and p2 == len(s2):
                    return True
                else:
                    return False
            if (p1, p2) in memo:
                return memo[(p1, p2)]
            a = b = False
            if p1 < len(s1) and s1[p1] == s3[p3]:
                a = solve(p1 + 1, p2, p3 + 1)

            if p2 < len(s2) and s2[p2] == s3[p3]:
                b = solve(p1, p2 + 1, p3 + 1)
            memo[(p1, p2)] = a or b
            return a or b

        return solve(0, 0, 0)

