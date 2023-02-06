class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        tSum = sum(nums)

        lSum = 0
        for i in range(len(nums)):
            rSum = tSum - nums[i] - lSum
            if lSum == rSum:
                return i

            lSum += nums[i]

        return -1


s = Solution()
print(s.pivotIndex([-1,-1,0,1,1,0]))
