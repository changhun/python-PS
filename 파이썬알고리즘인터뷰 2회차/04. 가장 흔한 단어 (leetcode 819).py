import re
import collections
import sys

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        """
        words = list(re.sub("[^a-zA-Z]", " ", paragraph).lower().split())
        words = [word for word in words if word not in banned]
        """
        words = [word for word in re.sub("[^a-zA-Z]", " ", paragraph).lower().split() if word not in banned]

        """ ver 1 """
        """
        counter = collections.defaultdict(int)
        for word in words:
            counter[word] += 1        
        max_value = 0
        for key, value in counter.items():
            if value > max_value:
                ans = key
                max_value = value
        print(ans)
        return ans
        """

        """ ver 2 """
        #"""
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]
        #"""

        """ ver 3 """
        """
        counter = collections.Counter(words)
        ans = max(counter, key=counter.get)
        return ans
        """

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
#Solution().mostCommonWord(paragraph, banned)
ret = Solution().mostCommonWord(paragraph, banned)
print(ret)

"""
words = paragraph.split()
print(type(words), words)
"""