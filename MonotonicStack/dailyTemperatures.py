#!/usr/bin/python3
"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemperature, stackIndex = stack.pop()
                answer[stackIndex] = index - stackIndex
            stack.append([temperature, index])

        return answer
