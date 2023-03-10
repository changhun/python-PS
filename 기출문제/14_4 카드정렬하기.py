import heapq

def solution(cards):
    heapq.heapify(cards)
    cards_num = len(cards)
    for i in range(cards_num - 1):
        min_card1 = heapq.heappop(cards)
        min_card2 = heapq.heappop(cards)
        heapq.heappush(heap, min_card1 + min_card2)

    return heap[0]

N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input))

ret = solution(cards)
print(ret)