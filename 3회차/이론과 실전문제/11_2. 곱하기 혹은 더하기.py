num_str = input()

ans = int(num_str[0])
for c in num_str[1:]:
    num = int(c)
    if ans <= 1 or num <= 1:
        ans += num
    else:
        ans *= num
print(ans)