data = input()

#alphas = ""
alphas = []
sum_value = 0
for c in data:
    if c.isalpha():
        alphas.append(c)
    elif c.isdigit():
        sum_value += int(c)

#print(alphas, sum_value)
alphas.sort()
ans = ''.join(alphas) + str(sum_value)
print(ans)

# INPUT
# AJKDLSI412K4JSJ9D
# K1KA5CB7