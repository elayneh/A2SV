"""
Given an array of unsorted numbersm find all unique triples in it that add up to zero\

"""
class Solution:
    def findTriplets(self, arr):
 
        found = False
        n = len(arr)
        # sort array elements
        nums = arr

        arr = sorted(arr)
        result = []
    
        for i in range(0, n-1):
        
            # initialize left and right
            l = i + 1
            r = n - 1
            x = arr[i]
            while (l < r):
            
                if (x + arr[l] + arr[r] == 0):
                    idx = nums.index(arr[i])
                    left = nums.index(arr[l])
                    right = nums.index(arr[r])
                    result.append([idx, left, right])
                    l += 1
                    r -= 1
                    found = True
    
                # If sum of three elements is less
                # than zero then increment in left
                elif (x + arr[l] + arr[r] < 0):
                    l += 1
    
                # if sum is greater than zero then
                # decrement in right side
                else:
                    r -= 1
    
        if (found == False):
            return " No Triplet Found"

        return result
