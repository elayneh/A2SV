#!/usr/bin/python3
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

class Solution:

    def isValid(self, s: str)-> bool:
        open_list = ["[","{","("]
        close_list = ["]", "}", ")"]

        stack = []

        for item in s:
            if item in open_list:
                stack.append(item)
            elif item in close_list:
                pos = close_list.index(item)
                if len(stack) > 0 and open_list[pos] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False


        if len(stack) == 0:
            return True
        else:
            return False
