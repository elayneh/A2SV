class Solution():
    def rotate(self, nums: list, k: int):
        n = len(nums)
        for i in range(k):
            next = nums[-1]
            for j in range(n):
                nums[j], next = next, nums[j]

        return nums

s = Solution()
print(s.rotate([-1,-100,3,99], 3))
