# usr/bin/python3

"""Works well for small files(with large value and small keys)
Requires no additional storage space
Doesn't scale well O(n2)
"""

#User function Template for python3

class Solution:
    def select(self, arr, i):
        for i in range(arr):
            return arr[i]

    def selectionSort(self, arr,n):
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr



#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input("How many arrays are You want to sort:\n"))
    for _ in range(t):
        n = int(input("Enter array length:\n"))
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
