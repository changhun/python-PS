import collections

class Solution:


    """ ver2

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
    """

    def anagrams(self, words:list)->list:
        dic = collections.defaultdict(list)
        for word in words:
            dic[''.join(sorted(word))].append(word)

        return dic.values()

sol = Solution()
strs = ["ate", "tea", "tan", "ate", "nat", "bat"]
print(sol.anagrams(strs))