def do_solution(s, comp_len):
    ans = 0
    ans_str = ""
    idx = 0
    while idx <= len(s) - comp_len:
        refer = s[idx : idx + comp_len]
        same_cnt = 1
        cur_pos = idx + comp_len
        while cur_pos <= len(s) - comp_len:
            # 문자열 비교 이렇게 하면 되는지?
            if refer != s[cur_pos:cur_pos + comp_len]:
                break
            cur_pos += comp_len
            same_cnt += 1

        ans += comp_len
        if same_cnt > 1:
            ans += len(str(same_cnt))
            ans_str += str(same_cnt)
        #idx = cur_pos + comp_len # cur_pos 는 이미 comp_len 만큼 더해져 있다.
        idx = cur_pos
        ans_str += refer

    ans += len(s) - idx
    ans_str += s[idx:]
    #print(ans_str)
    return ans


def solution(data):
    ans = len(data)
    for length in range(1, len(data) // 2 + 1):
        ret = do_solution(data, length)
        ans = min(ans, ret)
    return ans

s = input()
ans = len(s)
for length in range(1, len(s)//2 + 1):
    ret = solution(s, length)
    ans = min(ans, ret)
print(ans)


""" 옛날 제출된 코드 저장
INF = int(1e9)


def solution(data):
    if len(data) == 1:
        return 1

    ans = INF
    for sub_length in range(1, len(data)//2 + 1):
        sub_ans = len(data) % sub_length
        sub_str = data[0:sub_length]
        dup_cnt = 1

        for i in range(1, len(data)//sub_length):
            if sub_str == data[i*sub_length:(i+1)*sub_length]:
                dup_cnt += 1
            else:
                if dup_cnt == 1:
                    sub_ans += sub_length
                else:
                    sub_ans += len(str(dup_cnt)) + sub_length
                    dup_cnt = 1
                sub_str = data[i*sub_length:(i+1)*sub_length]

        # 마지막 거 정산
        sub_ans += sub_length
        if dup_cnt != 1:
            sub_ans += len(str(dup_cnt))
        ans = min(ans, sub_ans)
    return ans


"""

