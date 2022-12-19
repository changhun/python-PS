INF = int(1e9)
data = input()

#print(data[0:2])

ans = INF
for sub_length in range(1, len(data)//2):
    sub_ans = 0
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

print(ans)




