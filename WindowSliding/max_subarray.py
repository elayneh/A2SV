#!/usr/bin/python3


def maxSum(l, n, k):
    window_sum = sum(l[:k])
    max_sum = window_sum

    for i in range(n - k):
        window_sum =  window_sum - l[i] + l[k + i]
        max_sum = max(max_sum, window_sum)


    return max_sum

arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
n = len(arr)

print(maxSum(arr, n, 4))

