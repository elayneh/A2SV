"""
You are given an integer array arr. You can choose a set of integers and
remove all the occurences of these integers in the array.

Return the minimum size the set so that at least half of the integers of the array are removed.
"""

from collections import Counter # A Counter is a dict subclass for counting hashable objects.
                                # It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.


class Solution:
    def minSetSize(self, arr: list[int]) -> int:

        counter = Counter(arr)
        freq = sorted(counter.values(), reverse=True)
        print(freq)

        half_size = len(arr) // 2
        noSets = 0

        while half_size > 0:
            half_size -= freq[noSets]
            noSets += 1

        return noSets



s = Solution()
print(s.minSetSize([3,3,3,3,5,5,5,2,2,7]))
