s = input()
length = len(s)

switch_cnt = 1
for i in range(1, length):
    if s[i] != s[i-1]:
        switch_cnt += 1
print(switch_cnt//2)