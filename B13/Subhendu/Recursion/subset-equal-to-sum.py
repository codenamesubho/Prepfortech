"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Example:

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False There is no subset that add up to 30.

"""

def solution(arr, sum):

    def solve(idx, target):
        if target == 0:
            return True

        if target < 0 or idx > len(arr) -1:
            return False

        return solve(idx +1, target-arr[idx]) or solve(idx + 1, target)

    return solve(0, sum)


