INF = int(1e9)
PLUS = 0
MINUS = 1
MULTI = 2
DIVIDE = 3

global max_val, min_val
max_val = -INF
min_val = INF


def calculate(a:int, b:int, operator:int):
    if operator == PLUS:
        return a + b
    elif operator == MINUS:
        return a - b
    elif operator == MULTI:
        return a * b
    elif operator == DIVIDE:
        return int(a/b)


def dfs(cur_idx, nums, operators, calculated_value):
    global max_val, min_val

    if cur_idx >= len(nums):
        max_val = max(max_val, calculated_value)
        min_val = min(min_val, calculated_value)

        return

    for operator in range(4):
        if operators[operator] > 0:
            operators[operator] -= 1
            next_value = calculate(calculated_value, nums[cur_idx], operator)
            dfs(cur_idx + 1, nums, operators, next_value)
            operators[operator] += 1


N = int(input())
nums = list(map(int, input().split()))
operator_cnts = list(map(int, input().split()))

dfs(1, nums, operator_cnts, nums[0])

print(max_val)
print(min_val)
