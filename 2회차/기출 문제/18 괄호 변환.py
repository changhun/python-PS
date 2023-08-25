
def is_right(s):
    balance = 0
    for c in s:
        if c == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                return False

    return balance == 0


def flip(s):
    flipped = ""
    for i in range(len(s)):
        if s[i] == '(':
            flipped += ')'
        else:
            flipped += '('

    return flipped

def solution(s):
    if is_right(s):
        return s

    balance = 0
    i = 0
    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            break
    u = s[:i+1]
    v = s[i+1:]
    if is_right(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + flip(u[1:-1])

s = input()
ret = solution(s)
print(ret)
