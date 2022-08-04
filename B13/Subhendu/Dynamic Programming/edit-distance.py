class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ### https://leetcode.com/problems/edit-distance/
        def help(l1, l2):
            if l1 == 0: return l2
            if l2 == 0: return l1

            if word1[l1 - 1] == word2[l2 - 1]:
                return help(l1 - 1, l2 - 1)

            return min(help(l1 - 1, l2), help(l1, l2 - 1), help(l1 - 1, l2 - 1)) + 1

        return help(len(word1), len(word2))