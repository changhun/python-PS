import re
import collections
import sys

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
