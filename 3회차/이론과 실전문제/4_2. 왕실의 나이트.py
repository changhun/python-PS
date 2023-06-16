position = input()
low, col = int(position[1]), ord(position[0]) - ord('a') + 1

dy = [-2, -2, -1, 1, 2, 2, 1, -1]
dx = [-1, 1, 2, 2, 1, -1, -2, -2]

count = 0
for di in range(8):
    y = low + dy[di]
    x = col + dx[di]
    if y < 1 or y > 8 or x < 1 or x > 8:
        continue
    count += 1

print(count)