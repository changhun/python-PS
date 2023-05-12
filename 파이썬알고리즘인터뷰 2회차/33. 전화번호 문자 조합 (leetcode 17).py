class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = [""]*10
        mapping[2] = "abc"
        mapping[3] = "def"
        mapping[4] = "ghi"
        mapping[5] = "jkl"
        mapping[6] = "mno"
        mapping[7] = "pqrs"
        mapping[8] = "tuv"
        mapping[9] = "wxyz"

        ans = []
        comb = []
        def dfs(start):
            if start >= len(digits):
                ans.append(''.join(comb))
                return

            for char in mapping[int(digits[start])]:
                comb.append(char)
                dfs(start + 1)
                comb.pop()

        if digits:
            dfs(0)
        return ans


digits = "23"
digits = ""
ret = Solution().letterCombinations(digits)
print(ret)