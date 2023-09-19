class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()
        return s



s = ["h","e","l","l","o"]
ret = Solution().reverseString(s)
print(ret)