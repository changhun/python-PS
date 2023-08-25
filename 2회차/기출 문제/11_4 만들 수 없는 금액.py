import sys
input = sys.stdin.readline

N = int(input())
coins = list(map(int, input().split()))
coins.sort()

# max_val 은 현재 만들수 있는 최대값이다. 0 ~ max_val 은 모두 만들 수 있다.
max_val = 0
for coin in coins:
    # 현재 0 ~ max_val 의 숫자를 모두 만들 수 있기 때문에 새로운 화폐가 max_val + 1 이하라면 0 ~ max_val + coin 의 값을 모두 만들 수 있다.
    # 예를 들어 max_val + 1 의 값을 새로 만들어 보자. 기존의 코인만으로 max_val + 1 - coin 라는 숫자는 만들 수 있다. 여기에 새로운 코인을 사용하면 max_val + 1 의 값을 만들 수 있다.
    # 이를 일반화 하면 기존의 코인만으로 (max_val + 1 - coin) ~ max_val 범위의 값을 모두 만들 수 있고, 여기에 새로운 coin 을 더하면 (max_val + 1) ~ (max_val + coin)
    # 범위의 숫자를 모두 만들 수 있는 것이다. 기존의 코인만으로 0 ~ max_val 까지도 만들 수 있으므로 새로운 코인의 추가로 0 ~ max_val + coin
    # 의 범위가 커버된다.
    if coin > max_val + 1:
        break
    max_val += coin

print(max_val + 1)


