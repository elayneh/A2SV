#!/usr/bin/python3
"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n % 4 == 0:
            return self.isPowerOfFour(n // 4)
        if n == 1:
            return True
        else:
            return False
