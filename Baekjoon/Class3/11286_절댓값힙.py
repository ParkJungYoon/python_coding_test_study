import sys
input = sys.stdin.readline
import heapq
heap = []
n = int(input())

for i in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(num),num))