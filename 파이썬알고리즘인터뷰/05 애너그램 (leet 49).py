import collections

"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = collections.defaultdict(list)
        for word in strs:
            #dic[word.sort()].append(word)
            #dic[sorted(word)].append(word)
            dic[''.join(sorted(word))].append(word)

        answer = []
        for key, value in dic.items():
            answer.append(value)
        return answer
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = collections.defaultdict(list)
        for word in strs:
            dic[''.join(sorted(word))].append(word)

        return dic.values()

strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
ret = sol.groupAnagrams(strs)
print(ret)