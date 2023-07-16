def solution(s):
    if not s:
        return s
    count = 0
    u, v = "", ""
    for i, c in enumerate(s):
        if c == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            u = s[:i + 1]
            v = s[i + 1:]
            break

    is_right = True
    count = 0
    for c in u:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            is_right = False
            break
    if is_right:
        return u + solution(v)
    u_prime = []
    for c in u[1:-1]:
        if c == '(':
            u_prime += ')'
        else:
            u_prime += '('
    return '(' + solution(v) + ')' + ''.join(u_prime)


s = "(()())()"
s = ")("
s = "()))((()"
ret = solution(s)
print(ret)