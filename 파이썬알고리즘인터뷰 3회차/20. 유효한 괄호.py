class Solution:
    def isValid(self, s: str) -> bool:
        #l = list(s)

        l = []
        pair = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for ch in s:
            if ch in "({[":
                l.append(ch)
            else:
                if not l or l[-1] != pair[ch]:
                    return False
                l.pop()
        if l:
            return False
        return True




s = "()[]{}"
s = "()"
s = "(]"
ret = Solution().isValid(s)
print(ret)