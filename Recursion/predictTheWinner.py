class Solution():
    def PridictWinner(self, nums: list[int]) -> bool:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

        p1 = self.solve(nums, 0, len(nums) - 1)
        p2 = sum - p1
        if p1 < p2:
            return False

        return True

    def solve(self, nums, i, j):
        if i > j:
            return False
        option1 = nums[i] + min(self.solve(nums, i+2, j), self.solve(nums,i + 1, j -1))
        option2 = nums[j] +min(self.solve(nums, i+1, j-1), self.solve(nums, i, j-2))

        return max(option1, option2)
