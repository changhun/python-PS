

def split(s):
    cnt = 0
    i = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            break
    return s[:i+1], s[i+1:]

def correct(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False

    return cnt == 0


def reversing(s):
    ret = ''
    for c in s:
        if c == '(':
            ret += ')'
        elif c == ')':
            ret += '('
    return ret

def solution(s):
    if len(s) == 0:
        return s
    u ,v = split(s)
    if correct(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reversing(u[1:-1])

s = input()
