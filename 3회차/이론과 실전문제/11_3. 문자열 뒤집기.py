s = input()
condensed_s = [s[0]]
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        condensed_s.append(s[i])

print(len(condensed_s)//2)