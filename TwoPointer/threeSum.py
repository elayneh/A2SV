"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
 
        n = len(nums)

        nums = sorted(nums)
        res = []
    
        for i in range(0, n-2):        
            left = i + 1
            right = n - 1
            x = nums[i]
            while (left < right):
                if x + nums[left] + nums[right] == 0:
                    item = [nums[i], nums[left], nums[right]]
                    res.append(item) if item not in res else ...
                    left += 1
                    right -= 1

                elif x + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return res
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
