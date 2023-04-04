# 방법 1 bfs : 연결되어 있는지만 확인하면 됨 
# 시간 : 100ms
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

def bfs(start):
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for i in range(n):
            if result[start][i] == 0 and graph[cur][i] == 1:
                result[start][i] = 1
                queue.append(i)

for i in range(n):
    bfs(i)

for re in result:
    print(*re)

'''
# 방법 2 : 플로이드 워셜 알고리즘
# 시간 : 228ms

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for g in graph:
    print(*g)


'''

'''
0 1 0
0 0 1
1 0 0
(0,1)
(1,2)
(2,0)

(0,1) -> (0,1)
(0,1) -> (1,2) : (0,2)
(0,1) -> (1,2) -> (2,0) : (0,0)

bfs(0)
start = 0
0이랑 연결된거 찾아서 queue
'''