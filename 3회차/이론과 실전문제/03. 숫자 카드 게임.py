n, m = map(int, input().split())
cards = []
for _ in range(n):
    cards.append(list(map(int, input().split())))

print(max([min(low) for low in cards]))

# Input
# 2 4
# 7 3 1 8
# 3 3 3 4
#
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2