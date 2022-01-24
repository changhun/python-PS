import collections
import re

class Solution:


    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        re.sub('[^a-z0-9]', '', low)
        return low == low[::-1]

s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))