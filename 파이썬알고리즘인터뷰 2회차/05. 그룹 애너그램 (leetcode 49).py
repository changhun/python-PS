import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = collections.defaultdict(list)
        for word in strs:
            dic[str(sorted(word))].append(word)

        return dic.values()
        """
        ans = []
        for value in dic.values():
            ans.append(value)
        return ans
        """


strs = ["eat","tea","tan","ate","nat","bat"]
ret = Solution().groupAnagrams(strs)
print(ret)

print(type(sorted(strs[0])))
print(type(reversed(strs[0])))