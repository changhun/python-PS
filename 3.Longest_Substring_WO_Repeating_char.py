import collections

class Solution:


    def max_len(self, s:str)->int:
        ans = 0
        cur_len = 0
        first = 0
        cnt = collections.defaultdict(int)

        for i in range(len(s)):
            if cnt[s[i]] != 0:
                while s[first] != s[i]:
                    cnt[s[first]] -= 1
                    first += 1
                    cur_len -= 1
                cnt[s[first]] -= 1
                first += 1
                cur_len -= 1

            cnt[s[i]] += 1
            cur_len += 1
            if cur_len > ans:
                ans = cur_len

        return ans

sol = Solution()
s = "abcabcbb"
print(sol.max_len(s))

