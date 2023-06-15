import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = list(re.sub('[^a-zA-Z]', ' ', paragraph).lower().split())
        words = [word for word in words if word not in banned]
        print(words)
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
ret = Solution().mostCommonWord(paragraph, banned)
print(ret)