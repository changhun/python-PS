import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            word_sorted = ''.join(sorted([ch for ch in word]))
            # anagrams[[ch for ch in word].sort()].append(word)
            anagrams[word_sorted].append(word)
        return list(anagrams.values())



strs = ["eat","tea","tan","ate","nat","bat"]
ret = Solution().groupAnagrams(strs)
print(ret)