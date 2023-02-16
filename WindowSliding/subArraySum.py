#!/usr/bin/python3
"""
"""

class Solution():
    def subArraySum(self, nums: list[int], k: int) -> list[int]:
        resArr = [None] * (len(nums) - k + 1)
        windowStart = 0
        currWindowSum = 0
        for windowEnd in range(len(nums)):
            currWindowSum += nums[windowEnd]
            while windowEnd - windowStart == k -1:
                resArr[windowStart] = currWindowSum
                currWindowSum -= resArr[windowStart]
                windowStart += 1

        return resArr


s = Solution()
print(s.subArraySum([4,3,2,6,34,11,5], 3))

