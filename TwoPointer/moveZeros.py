#!/usr/bin/python3

"""

"""
class Solution():
    def moveZeros(self, nums: list[int]):

        if len(nums) <= 0:
            return

        ptr = 0
        for num in nums:
            if num != 0:
                nums[ptr] = num
                ptr += 1

        while ptr < len(nums):
            nums[ptr] = 0
            ptr += 1

        return nums
