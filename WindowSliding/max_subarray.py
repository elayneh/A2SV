#!/usr/bin/python3


def maxSumArray(nums: list[int], k: int) -> int:

    win_sum = sum(nums[:k])
    max_sum = win_sum

    for i in range(len(nums) - k):
            win_sum += nums[k + i] - nums[i]
            max_sum = max(max_sum, win_sum)

    return max_sum


print(maxSumArray([21,3,6,76,4,56], 2))
