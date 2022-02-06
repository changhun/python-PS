import collections


class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
    #def letter_combination(self, phone_num : str):
        def dfs(idx : int, path:str):
            if idx == len(digits):
                ans.append(path)
                return

            for i in range(len(num_2_char[digits[idx]])):
                dfs(idx+1, path + num_2_char[digits[idx]][i])


        num_2_char = {
             "2": "abc",
             "3": "def",
             "4": "ghi",
             "5": "jkl",
             "6": "mno",
             "7": "pqrs",
             "8": "tuv",
             "9": "wxyz"
        }
        #ans = [str]
        ans = []
        #s = [str]

        if not digits:
            return []

        dfs(0, "")
        #print(ans)
        return ans

num = "23"
sol = Solution()

sol.letterCombinations(num)