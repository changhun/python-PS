import re
import collections
import sys

"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = list(re.sub('[^a-z]', ' ', paragraph.lower()).split())
        dic = collections.defaultdict(int)

        for word in words:
            if word not in banned:
                dic[word] += 1

        max_value = -sys.maxsize
        max_word = ""
        for key, value in dic.items():
            if value > max_value:
                max_value = value
                max_word = key

        return max_word
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub("[^\w]", ' ', paragraph).lower().split() if word not in banned]
        #words = [word for word in re.sub("[^a-zA-Z]", ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol = Solution()
ans = sol.mostCommonWord(paragraph, banned)
print(ans)
