class Solution:
    def kthLargestNumber(self, nums: list, k: int)-> str:
        nums = [int(item) for item in nums]

        # for i in range(len(nums)):
        #     for j in range(len(nums)- i - 1):
        #         if(nums[j] > nums[j + 1]):
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        nums.sort()

        print(nums)
        return "{}".format(str(nums[-k]))




s = Solution()
s.kthLargestNumber([34,2,4,2,54], 3)
