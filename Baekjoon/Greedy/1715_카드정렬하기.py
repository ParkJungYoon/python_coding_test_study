# 문제해결 아이디어
# 기존 합에서 카드를 비교하는게 최소인지 아직 비교하지 않은 카드끼리 비교하는게 최소인지 생각함.
# 내가 생각한 알고리즘은 힙에서 최소값 2개를 꺼내서 비교하고 그 값을 다시 힙에 push함. 그리고 다시 최소값 2개 pop.
import sys
import heapq
input = sys.stdin.readline
n = int(input())
card = []
for i in range(n):
    heapq.heappush(card,int(input()))

result = 0
while len(card) > 1:
    now1 = heapq.heappop(card)
    now2 = heapq.heappop(card)
    result += (now1 + now2)
    heapq.heappush(card,now1+now2)
print(result)
