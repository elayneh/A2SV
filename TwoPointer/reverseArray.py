#!/usr/bin/python3

"""

"""
class Solution():
    def reverseArray(self, nums: list[int]) -> list[int]:

        end = len(nums) - 1
        start = 0
        while start < end:
            nums[end], nums[start] = nums[start], nums[end]
            end -= 1
            start += 1

        return nums
