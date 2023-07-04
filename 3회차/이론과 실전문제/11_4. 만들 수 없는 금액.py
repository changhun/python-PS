n = int(input())
coins = list(map(int, input().split()))
max_range = 0

coins.sort()
for coin in coins:
    if coin > max_range + 1:
        break
    max_range += coin
print(max_range + 1)