import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        replaced = re.sub("[^a-zA-Z0-9]","", s).lower()
        return replaced == replaced[::-1]

s = "A man, a plan, a canal: Panama"
s = "race a car"
ret = Solution().isPalindrome(s)
print(ret)