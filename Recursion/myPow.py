#!/usr/bin/python3
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

class Solution():
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or n == 0:
            return 1
        elif n == 1:
            return x
        res = x * pow(x, n-1)
        return float("%.5f" %res)

