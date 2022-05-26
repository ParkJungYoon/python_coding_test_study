import sys
# import heapq
input = sys.stdin.readline
n = int(input())
# 메모리 초과
# heap = []
# for i in range(n):
#     heapq.heappush(heap,int(input()))
# for i in range(n):
#     print(heapq.heappop(heap))

num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)