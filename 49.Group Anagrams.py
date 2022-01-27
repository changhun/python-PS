import collections

class Solution:


    def anagrams(self, words:list)->list:
        dic = {}
        anagram_cnt = 0
        ans = []
        for word in words:
            sorted_word = word.sort()
            if sorted_word in dic:
                ans[dic[sorted_word]].append(word)
            else:
                dic[sorted_word] = anagram_cnt
                anagram_cnt += 1
                ans.append(list(word))
        return ans

sol = Solution()
strs = ["ate", "tea", "tan", "ate", "nat", "bat"]
print(sol.anagrams(strs))