import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            dic[''.join(sorted(s))].append(s)

        return dic.values()

strs = ["eat","tea","tan","ate","nat","bat"]
ret = Solution().groupAnagrams(strs)
print(ret)