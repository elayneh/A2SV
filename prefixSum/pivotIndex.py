#!/usr/bin/python3

"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        tSum = sum(nums)

        lSum = 0
        for i in range(len(nums)):
            rSum = tSum - nums[i] - lSum
            if lSum == rSum:
                return i

            lSum += nums[i]

        return -1


s = Solution()
print(s.pivotIndex([-1,-1,0,1,1,0]))
