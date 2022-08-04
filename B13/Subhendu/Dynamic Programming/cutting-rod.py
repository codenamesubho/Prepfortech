# User function Template for python3

class Solution:
    def cutRod(self, price, n):
        ### https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
        # code here
        memo = {}

        def help(size):
            if size == 0:
                return 0
            if size in memo:
                return memo[size]

            p = float('-inf')
            for i in range(1, n + 1):
                if size - i >= 0:
                    p = max(p, price[i - 1] + help(size - i))
            memo[size] = p
            return p

        return help(n)