"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.
"""
class Solution:
    def minPairSum(self, nums: list[int])-> int:
        sorted_arr = sorted(nums)
        reversed_sorted_arr = sorted(nums, reverse=True)
        sum = []

        for a, b in zip(sorted_arr, reversed_sorted_arr):
            sum.append(a+b)

        return max(sum)
