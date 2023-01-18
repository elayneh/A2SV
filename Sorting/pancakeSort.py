class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        res = []
        for i in range(len(arr), 1, -1):
            idx = arr.index(i)
            res.extend([idx + 1, i])
            arr = arr[:idx:-1] + arr[:idx]
        return res


s =Solution()
print(s.pancakeSort([1,2,3]))
