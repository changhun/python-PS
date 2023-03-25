import sys
input = sys.stdin.readline
import heapq

N = int(input())
#cards = list(map(int, input().split()))
cards = []
for i in range(N):
    cards.append(int(input()))

heapq.heapify(cards)

ans = 0
for i in range(N-1):
    min_val1 = heapq.heappop(cards)
    min_val2 = heapq.heappop(cards)
    sum_of_two_cards = min_val1 + min_val2
    ans += sum_of_two_cards
    heapq.heappush(cards, sum_of_two_cards)
    #print(min_val1, min_val2)

print(ans)