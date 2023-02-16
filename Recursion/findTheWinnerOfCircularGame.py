#!/usr/bin/python3
"""
here are n friends that are playing a game.
The friends are sitting in a circle and are numbered from 1 to n in clockwise order
More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n,
 and moving clockwise from the nth friend brings you to the 1st friend.

"""

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
       return self.findWinnerHelper(n, k - 1) + 1
    def findWinnerHelper(self, n, k):
        if n == 1:
            return 0
        return ((k + 1) % n + self.findWinnerHelper(n - 1, k)) % n


s = Solution()
print(s.findWinner(90, 5))
