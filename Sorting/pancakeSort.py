"""
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.
length flips will be judged as correct.


"""

class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        res = []
        for item in range(len(arr), 1, -1):
            idx = arr.index(item) # to get the indext of the list item
            res.extend([idx + 1, item]) # to sum up list to list res
            arr = arr[:idx:-1] + arr[:idx]
        return res

s =Solution()
print(s.pancakeSort([1,2,3]))
