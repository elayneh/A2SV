#!/usr/bin/python3

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
class Solution:
    def productExeptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        preFix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        postFix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postFix
            postFix *= nums[i]

        return result
