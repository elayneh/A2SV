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
