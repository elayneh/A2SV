#!/usr/bin/python3
"""
"""

class Solution():
    def removeElement(self, nums: list[int], val: int) -> list[int]:
        if len(nums) == 0:
            return 0
        ptr = 0
        for num in nums:
            if num != val:
                nums[ptr] = num
                ptr +=  1
                
        return ptr
