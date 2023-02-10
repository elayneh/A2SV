#!/usr/bin/python3

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        currSum = 0
        prefixSum = {0 : 1}
        for i in nums:
            currSum += nums
            diff = currSum - k

            result += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)

        return result



