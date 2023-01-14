def buble_sorter(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums [j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

arr = [2,0,2,1,1,0]
print(buble_sorter(arr))
