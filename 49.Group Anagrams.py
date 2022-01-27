import collections

class Solution:


    def anagrams(self, words:list)->list:
        dic = {}
        anagram_cnt = 0
        ans = []
        for word in words:
            if ''.join(sorted(word)) in dic:
                ans[dic[''.join(sorted(word))]].append(word)
            else:
                dic[''.join(sorted(word))] = anagram_cnt
                anagram_cnt += 1
                #ans.append(list(word))
                ans.append([word])
        return ans

sol = Solution()
strs = ["ate", "tea", "tan", "ate", "nat", "bat"]
print(sol.anagrams(strs))