import collections

class Solution:
    def permute(self, l:list[int])->list[list[int]]:
        def dfs(idx:int):
            #print(idx)
            #print(path)
            if len(l) == idx:
                #print(path)
                #print(ans)
                #ans.append(path)
                # 리스트에 append 하면 추가된 인자는 참조형인가?
                # ans 에 path 추가하고나서 caller 에서 path.pop() 하면 ans를 구성하는 요소도 바뀌어 있다!!!
                ans.append(path[:])
                # path[:] 하면 참조 대신 복사됨?
                #print(ans)
                #print()
                return
            for num in l:
                #if num not in path:
                if num in path:
                    continue
                path.append(num)
                dfs(idx+1)
                path.pop()

        ans = []
        path = []

        if not l:
            return []

        dfs(0)
        #print(ans)
        return ans


sol = Solution()
l = [1, 2, 3]
sol.permute(l)