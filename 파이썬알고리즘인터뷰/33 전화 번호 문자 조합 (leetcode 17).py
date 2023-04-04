class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        mapping = [""] * 10
        mapping[2] = "abc"
        mapping[3] = "def"
        mapping[4] = "ghi"
        mapping[5] = "jkl"
        mapping[6] = "mno"
        mapping[7] = "pqrs"
        mapping[8] = "tuv"
        mapping[9] = "wxyz"
        """
        mapping = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        ans = []
        comb = []

        def dfs(start):
            if len(digits) == start:
                ans.append(''.join(comb))
                return

            for c in mapping[digits[start]]:
                comb.append(c)
                dfs(start + 1)
                comb.pop()

        if len(digits) == 0:
            return ans
        dfs(0)
        return ans


digits = "23"
ret = Solution().letterCombinations(digits)
print(ret)