import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = re.sub("[^a-zA-Z0-9]", '', s).lower()
        return t == t[::-1]



s = "A man, a plan, a canal: Panama"
ret = Solution().isPalindrome(s)
print(ret)