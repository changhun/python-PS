def compress(s, step):
    ans_str = ""
    prev = s[0:step]
    same_cnt = 1
    for pos in range(step, len(s), step):
        cur = s[pos:pos + step]
        if prev != cur:
            ans_str += str(same_cnt) + prev if same_cnt > 1 else prev
            prev = cur
            same_cnt = 1
        else:
            same_cnt += 1

    ans_str += str(same_cnt) + prev if same_cnt > 1 else prev
    #print(ans_str)
    return len(ans_str)


def solution(s):
    ans = len(s)
    for step in range(1, len(s)//2 + 1):
        ret = compress(s, step)
        ans = min(ans, ret)
    return ans


s = input()
ans = solution(s)
print(f'ans = {ans}')
