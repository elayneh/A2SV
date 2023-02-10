#!/usr/bin/python3

"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        length, total = 0, 0
        result = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                result = min(r - length + 1, result)
                total -= nums[length]
                length += 1

        return 0 if result == float("inf") else result
