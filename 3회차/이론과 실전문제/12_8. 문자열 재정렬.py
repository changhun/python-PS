s = input()
strs = []
num = 0
for c in s:
    if '0' <= c <= '9':
        num += int(c)
    else:
        strs.append(c)

print(''.join(sorted(strs)) + str(num))