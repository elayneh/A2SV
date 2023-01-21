#!/usr/bin/python3
"""
You are a string s that consists of lower case English letters and brackets

Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets

"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                inner = s[stack[-1]: i + 1]
                inner = inner[::-1]
                s = s[:stack[-1]] + inner + s[i+1:]
                del stack[-1]
        res = ""
        for i in range(n):
            if s[i] != '(' and s[i] != ')':
                res += s[i]

        return res
