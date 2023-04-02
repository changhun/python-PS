from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        n = len(grid)
        m = len(grid[0])
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '2'
                    q.append((i, j))

                    while q:
                        y, x = q.popleft()
                        for di in range(4):
                            ny = y + dy[di]
                            nx = x + dx[di]
                            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == '1':
                                grid[ny][nx] = '2'
                                q.append((ny, nx))
        return count
