n, m = map(int, input().split())
balls = list(map(int, input().split()))

weight_count = [0]*(m+1)
p_sum = [0]*(m+2)

for i in range(0, n):
    weight_count[balls[i]] += 1

for i in range(m, 0, -1):
    #print(i)
    p_sum[i] = p_sum[i+1] + weight_count[i]

#for i in range(1, m+1):
    #print(p_sum[i])

ans = 0
for i in range(1, m):
    ans += weight_count[i] * p_sum[i+1]
print(ans)


# Input
# 8 5
# 1 5 4 3 2 4 5 2
#
# 5 3
# 1 3 2 3 2

