#!/usr/bin/python3

"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

"""
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            curr_val = nums2[i]
            while stack and curr_val > stack[-1]:
                idx = nums1Idx[stack.pop()]
                result[idx] = curr_val
            if curr_val in nums1Idx:
                stack.append(curr_val)

        return result
