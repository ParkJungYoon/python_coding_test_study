import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    x, y = map(int,input().split())
    heapq.heappush(heap,(x, y))
while heap:
    print(*heapq.heappop(heap))