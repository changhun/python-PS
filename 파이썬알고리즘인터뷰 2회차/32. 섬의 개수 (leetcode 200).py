''' sol1: dfs (recursive) '''
"""
LAND = '1'
WATER = '0'

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(sy, sx):
            grid[sy][sx] = WATER
            dy = [-1, 0, 1, 0]
            dx = [0, 1, 0, -1]

            for di in range(4):
                ny = sy + dy[di]
                nx = sx + dx[di]
                if ny < 0 or ny >= n:
                    continue
                if nx < 0 or nx >= m:
                    continue
                if grid[ny][nx] == LAND:
                    dfs(ny, nx)

        n = len(grid)
        m = len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == LAND:
                    dfs(i, j)
                    ans += 1
        return ans
"""

''' sol2: dfs (iterative) '''
#"""
LAND = '1'
WATER = '0'

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(sy, sx):
            dy = [-1, 0, 1, 0]
            dx = [0, 1, 0, -1]

            stack = []
            stack.append((sy, sx))
            while stack:
                y, x = stack.pop()
                if grid[y][x] == WATER:
                    continue
                grid[y][x] = WATER
                for di in range(4):
                    ny = y + dy[di]
                    nx = x + dx[di]
                    if ny < 0 or ny >= n:
                        continue
                    if nx < 0 or nx >= m:
                        continue
                    if grid[ny][nx] == LAND:
                        stack.append((ny, nx))

        n = len(grid)
        m = len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == LAND:
                    dfs(i, j)
                    ans += 1
        return ans
#"""

''' sol3: bfs '''
"""
import collections
LAND = '1'
WATER = '0'

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def bfs(sy, sx):
            dy = [-1, 0, 1, 0]
            dx = [0, 1, 0, -1]
            q = collections.deque()
            q.append((sy, sx))
            grid[sy][sx] = WATER

            while q:
                y, x = q.popleft()

                for di in range(4):
                    ny = y + dy[di]
                    nx = x + dx[di]
                    if ny < 0 or ny >= n:
                        continue
                    if nx < 0 or nx >= m:
                        continue
                    if grid[ny][nx] == LAND:
                        q.append((ny, nx))
                        grid[ny][nx] = WATER

        n = len(grid)
        m = len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == LAND:
                    bfs(i, j)
                    ans += 1
        return ans
"""