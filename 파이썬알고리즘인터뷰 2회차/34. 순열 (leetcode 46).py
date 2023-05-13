class Solution:
    def permute(self, l:list[int])->list[list[int]]:
        ans = []
        def dfs(remain, sub_ans):
            if remain <= 0:
                ans.append(sub_ans[:])
                return

            for num in l:
                if num in sub_ans:
                    continue
                sub_ans.append(num)
                dfs(remain - 1, sub_ans)
                sub_ans.pop()

        def dfs2(remain, sub_ans):
            if remain <= 0:
                ans.append(sub_ans)
                return

            for num in l:
                if num in sub_ans:
                    continue
                # list + new element makes new list
                dfs(remain - 1, sub_ans + [num])

        dfs2(len(l), [])
        return ans


nums = [1, 2, 3]
ret = Solution().permute(nums)
print(ret)
