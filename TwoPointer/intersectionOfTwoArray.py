class Solution():
    def intersectionOfArray(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return 0

        res = []
        nums1.sort()
        nums2.sort()

        pointer = 0

        for i in range(len(nums1)):
            while pointer < len(nums2) - 1 and nums2[pointer] < nums1[i]:
                pointer += 1
            if pointer < len(nums2) and nums1[i] == nums2[pointer]:
                res.append(nums1[i])
                pointer += 1

        resArr = [0] * len(res)
        for i in range(len(res)):
            resArr[i] = res[i]

        return resArr


s = Solution()
print(s.intersectionOfArray([2,2,7], [2,7]))
print(s.intersectionOfArray([4,5, 9, 4], [9,4,9,8,4]))
