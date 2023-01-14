arr = [2,3,4,2,34,13]
aarr = [0] * (max(arr) + 1)
for num in arr:
    aarr[num] += 1

print(*aarr)
