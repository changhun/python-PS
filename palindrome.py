# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char)
#
#         while len(strs) > 1:
#             if strs.pop() != strs.pop(0):
#                 return False
#         return True

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]

sol = Solution()
s = "asdsa"
result = sol.isPalindrome(s)
print(result)
print(s)