# Given a list of non-negative numbers nums, arrange them.
# such that they form the largest number and return it
# Since the nums may be very large and u should return the string of an integer

def larger_finder(nums):
    if len(nums)==1:
        return str(nums[0])
    for i in range(len(nums)):
        nums[i]=str(nums[i])
    for i in range(len(nums)):
        for j in range(1+i,len(nums)):
            if nums[j]+nums[i]>nums[i]+nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    nums=''.join(nums)
    if(nums=='0'*len(nums)):
        return '0'

    return nums

if __name__ == "__main__":
    nums = [3,30,34,5,9]
    print(larger_finder(nums))
