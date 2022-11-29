import collections
import re

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
#                     if word not in banned]
#         counts = collections.Counter(words)
#         return counts.most_common(1)[0][0]






class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        strs = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                if word not in banned]

        counts = collections.Counter(strs)
        return counts.most_common(1)[0][0]




sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol.mostCommonWord(paragraph, banned))