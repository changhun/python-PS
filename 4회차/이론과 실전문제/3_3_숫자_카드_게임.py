n, m = map(int, input().split())
#print(n, m)

cards = [list(map(int, input().split())) for i in range(n)]

#for row in cards:
#    print(row)

ans = 0
for row in cards:
    ans = max(ans, min(row))

print(ans)
