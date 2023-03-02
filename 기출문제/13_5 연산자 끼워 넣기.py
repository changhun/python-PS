
PLUS = 0
MINUS = 1
MULTI = 2
DIVISION = 3

N = int(input())
operands = list(map(int, input().split()))
operator_nums = list(map(int, input().split()))
operator_sequence = []


def operator(a, b, op):
    if op == PLUS:
        return a + b
    elif op == MINUS:
        return a - b
    elif op == MULTI:
        return a * b
    elif op == DIVISION:
        if a < 0:
            return -(-a // b)
        else:
            return a // b

# 문자열 타입 변수 비교 어떻게?


def calc():
    prev = operands[0]
    for i in range(1, N):
        prev = operator(prev, operands[i], operator_sequence[i-1])

    return prev


def dfs(remain_operators, ans):
    if remain_operators == 0:
        ret = calc()
        # 아래처럼 왜 안되?
        #min_ans = min(min_ans, ret)
        #max_ans = max(max_ans, ret)

        ans[0] = min(ans[0], ret)
        ans[1] = max(ans[1], ret)



    # i in PLUS, MINUS, MULTI, DIVISION
    for i in range(4):
        if operator_nums[i] == 0:
            continue
        operator_sequence.append(i)
        operator_nums[i] -= 1
        dfs(remain_operators - 1, ans)
        operator_nums[i] += 1
        operator_sequence.pop(-1)

INF = 987654321
min_ans = 987654321
max_ans = -987654321
ans = [INF, -INF]
dfs(N-1, ans)
min_ans = ans[0]
max_ans = ans[1]
print(max_ans, min_ans)