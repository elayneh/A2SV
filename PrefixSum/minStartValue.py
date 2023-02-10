#!/usr/bin/python3

"""Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""

class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        sum = [0]
        for i in range(len(nums)):
            sum.append(sum[i] + nums[i])
        sum = sum[1:]
        if 1 - min(sum) < 1:
            return 1
        return 1 - min(sum)
