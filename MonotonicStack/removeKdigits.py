#!/usr/bin/python3

"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for counter in num:
            while k > 0 and stack and stack[-1] > counter:
                k -= 1
                stack.pop()
            stack.append(counter)
        stack = stack[:len(stack) - k]
        result = "".join(stack)
        return str(int(result))if result else "0"
