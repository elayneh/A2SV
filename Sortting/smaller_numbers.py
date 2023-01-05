# Given the array nums for rach nums[i] find our how many numbers in the array are smaller
# than it. This is or each nums[i] you havae to countthe numver of valid oj's such that j != i and nums[j] < nums[i]
from random import randint
import random



sCounter_list = []
def smaller_finder(nums):
    sCounter = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                sCounter = sCounter + 1
        sCounter_list.append(sCounter)
        sCounter = 0


    return sCounter_list

if __name__ == "__main__":
    n = int(input("Inter array length: "))
    initial = int(input("Inter range of Integers to be generated\n"))
    final = int(input())
    nums = [randint(initial, final)for i in range(n)]
    print(nums)
    print(smaller_finder(nums))
