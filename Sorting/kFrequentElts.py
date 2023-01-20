#!/usr/bin/python3
"""
Given an integer array nums and an integer k,
Return the k most frequent elements. You may return the answer in any order.
"""


import heapq
import collections
class Solution:
    def topKFrequent(self, nums: list[int], k: int)->list[int]:
        dic = collections.Counter(nums)
        kFreq = []

        for keys, values in dic.items():
            if len(kFreq) < k:
                heapq.heappush(kFreq, (values, keys))
            else:
                heapq.heappush(kFreq, (values, keys))
                heapq.heappop(kFreq)

        return [keys for values, keys in kFreq]
