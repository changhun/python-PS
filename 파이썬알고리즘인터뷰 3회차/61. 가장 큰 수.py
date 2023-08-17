from typing import List




class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        tmp = [0] * len(nums)

        def is_ok(i, j):
            return str(nums[i]) + str(nums[j]) >= str(nums[j]) + str(nums[i])

        def mergeSort(s, e):
            if s >= e:
                return
            m = (s + e) // 2
            mergeSort(s, m)
            mergeSort(m+1, e)

            i = s
            j = m + 1
            k = s
            while i <= m and j <= e:
                if is_ok(i, j):
                    tmp[k] = nums[i]
                    k += 1
                    i += 1
                else:
                    tmp[k] = nums[j]
                    k += 1
                    j += 1
            while i <= m:
                tmp[k] = nums[i]
                k += 1
                i += 1
            while j <= e:
                tmp[k] = nums[j]
                k += 1
                j += 1

            for k in range(s, e + 1):
                nums[k] = tmp[k]

        mergeSort(0, len(nums) -1 )
        ans = ""
        print(nums)
        for num in nums:
            ans += str(num)
        if nums[0] == 0:
            ans = "0"
        return ans


nums = [3,30,34,5,9]
ret = Solution().largestNumber(nums)
print(ret)