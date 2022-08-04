class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        memo = {}
        ### https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

        def help(target, idx):
            if n == idx or target == 0:
                return 0

            if (target, idx) in memo:
                return memo[(target, idx)]

            if (wt[idx] > target):
                op = help(target, idx + 1)

            else:
                op = max(val[idx] + help(target - wt[idx], idx + 1),
                         help(target, idx + 1))
            memo[(target, idx)] = op
            return op

        return help(W, 0)
        # code here