
def buble_sorter(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums [j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

def target_indece(arr, target):
    target_list = []
    if (len(arr)):
        arr = buble_sorter(arr)
    for i in range(len(arr)):
        if arr[i] ==target:
            target_list.append(i)
        target_list = buble_sorter(target_list)

    return target_list


target = int(input("please inter the targer element:\n"))
nums = [1,2,12,34,45,23,5,2,3]
print(target_indece(nums, target))
