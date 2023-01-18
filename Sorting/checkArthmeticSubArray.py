class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        d = {}
        res = []

        for i in range(len(l)):
            d[i] = nums[l[i]:r[i]+1]
        for item in d:
            j = 0
            d[item].sort()
            for i in range(2,len(d[item])):
                if d[item][i]-d[item][i-1]!=d[item][1]-d[item][0]:
                    res.append(False)
                    break
                j+=1
            if j==len(d[item])-2:
                res.append(True)
        return res
