
# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         left, right = 0, len(s) - 1
#         while left < right :
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1

class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()

sol = Solution()
#s = "hello python"
l = [1, 2, 3, 4, 5, 6]
print(l)
sol.reverseString(l)
print(l)