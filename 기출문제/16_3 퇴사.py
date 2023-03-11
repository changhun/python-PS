N = int(input())
cost = []
worth = []

for _ in range(N):
    c, w = map(int, input().split())
    cost.append(c)
    worth.append(w)


#for i in range(N-1, -1, -1):
# for i in range(N-2, -1, -1):
#     val1 = worth[i+1]
#     val2 = worth[i]
#     if i + cost[i] < N:
#         val2 += worth[i + cost[i]]
#     worth[i] = max(val1, val2)

for i in range(N-1, -1, -1):
    val1 = 0
    val2 = 0

    if i < N - 1:
        val1 = worth[i+1]

    if i + cost[i] - 1 < N:
        val2 = worth[i]

    if i + cost[i] < N:
        val2 += worth[i + cost[i]]

    worth[i] = max(val1, val2)

print(worth[0])