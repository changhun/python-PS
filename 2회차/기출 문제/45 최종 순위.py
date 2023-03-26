from collections import deque
import sys
input = sys.stdin.readline


def find_parent(a, parents):
    if parents[a] != a:
        parents[a] = find_parent(parents[a], parents)
    return parents[a]


def union_parent(a, b, parents):
    pa = find_parent(a, parents)
    pb = find_parent(b, parents)
    if pa < pb:
        parents[pb] = pa
    else:
        parents[pa] = pb


def dfs(start):
    #if visited[start]:
    #    return
    global count
    discovered[start] = count
    count += 1
    for i in range(1, n+1):
        if graph[start][i] == 1:
            if discovered[i] == -1:
                is_cycle = dfs(i)
                if is_cycle:
                    return True
            if discovered[i] < discovered[start] and not finished[i]:
                return True # cycle 발견

    finished[start] = True
    return False


tc = int(input())
for _ in range(tc):
    n = int(input())
    rank_team = list(map(int, input().split()))
    rank_team = [0] + rank_team
    team_rank = [0] * (n+1)

    for ranking in range(1, n+1):
        team = rank_team[ranking]
        team_rank[team] = ranking
    #team_rank 의 1 ~ n 은 team1~n 의 등수이다.

    #graph[i][j] ==1 이 의미하는 것은 team_i 가 team_j 를 이긴다는 의미
    graph = [[0] * (n+1) for _ in range(n+1)]
    for ranking in range(1, n+1):
        win_team = rank_team[ranking]
        for l_idx in range(ranking+1, n+1):
            lose_team = rank_team[l_idx]
            graph[win_team][lose_team] = 1
    #print(graph)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1 - graph[a][b]
        graph[b][a] = 1 - graph[b][a]

    # 서로 소로(find & union 자료구조) 순방향 싸이클을 확인할 수 없다!!
    """
    parents = [i for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1:
                pi = find_parent(i, parents)
                pj = find_parent(j, parents)
                if (pi == pj):
                    print("cycle")
                union_parent(i, j, parents)
    """
    global count
    count = 0
    discovered = [-1] * (n+1)
    finished = [False] * (n+1)
    is_cycle = False
    for i in range(1, n+1):
        if discovered[i] != -1:
            continue
        is_cycle = dfs(i)
        if is_cycle:
            break
    if is_cycle:
        print("IMPOSSIBLE")
    else:
        #위상정렬
        #print("test")
        in_degrees = [0] * (n+1)
        result = []
        for j in range(1, n+1):
            in_degree = 0
            for i in range(1, n+1):
                if graph[i][j] == 1:
                    in_degree += 1
            in_degrees[j] = in_degree

        q = deque()
        for i in range(1, n+1):
            if in_degrees[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            result.append(cur)

            for next in range(1, n+1):
                if graph[cur][next] == 1:
                    in_degrees[next] -= 1
                    if in_degrees[next] == 0:
                        q.append(next)
        #print(result)
        for i in range(n):
            print(result[i], end=" ")
        print()
