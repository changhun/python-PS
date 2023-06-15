""" sol1"""
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [char.lower() for char in s if char.isalnum()]
         return l == l[::-1]
"""
""" Sol 2 """
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]



s = "race a car"
s = "A man, a plan, a canal: Panama"
ret = Solution().isPalindrome(s)
print(ret)