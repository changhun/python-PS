import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())







sol = Solution()
strs = ["ate", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))