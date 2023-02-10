class NumArray:

    def __init__(self, nums: list[int]):
        if len(nums) == 0:
            return

        self.prefixSum = [0] * len(nums)
        self.prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefixSum[i] += self.prefixSum[i-1] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.prefixSum[right] - self.prefixSum[left - 1]
        else:
            return self.prefixSum[right]


n = NumArray([1,2,3,4,5,6,7,75])
print(n.sumRange(1, 3))
