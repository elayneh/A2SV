"""
You are given an integer array arr. You can choose a set of integers and
remove all the occurences of these integers in the array.

Return the minimum size the set so that at least half of the integers of the array are removed.
"""

from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:

        counter = Counter(arr)
        noFreq = sorted(counter.values(), reverse=True)

        half_size = len(arr) // 2
        res = 0

        while half_size > 0:
            half_size -= noFreq[res]
            res += 1

        return res



s = Solution()
print(s.minSetSize([3,3,3,3,3,3,3,3,3]))
