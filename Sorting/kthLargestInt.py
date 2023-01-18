class Solution:
    def kthLargestNumber(self, nums: list, k: int)-> str:
        for i in range(len(nums)):
            nums[i] = int(nums[i])

        for i in range(len(nums)):
            for j in range(len(nums)- i - 1):
                if(nums[j] > nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return "{}".format(str(nums[-k]))
