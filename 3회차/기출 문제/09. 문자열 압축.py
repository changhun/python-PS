INF = int(1e9)

def compress(s, step):
    st, dup_count, ans = 0, 1, 0
    n = len(s)
    for cur in range(step, n, step):
        if s[st:st + step] != s[cur : cur + step]:
            ans += step
            if dup_count != 1:
                ans += len(str(dup_count))
            st = cur
            dup_count = 1
        else:
            dup_count += 1

    if dup_count == 1:
        ans += n - st
    else:
        ans += len(str(dup_count)) + step

    return ans


def solution(s):
    half = len(s)//2
    ans = INF
    for step in range(1, half + 1):
        ans = min(ans, compress(s, step))
    return ans


s = "aabbaccc"
ans = solution(s)
print(ans)