#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(nums):
    swap_counter = 0
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums [j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap_counter = swap_counter + 1

    print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(swap_counter, nums[0], nums[-1]))

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
