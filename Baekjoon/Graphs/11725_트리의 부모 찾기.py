import sys
input = sys.stdin.readline
from collections import deque, defaultdict

n = int(input())

graph = defaultdict(list)
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

node = defaultdict(int)

def bfs():
    queue = deque([1])
    while queue:
        cur_node = queue.popleft()
        for i in graph[cur_node]:
            if node[i] == 0:
                node[i] = cur_node
                queue.append(i)

bfs()
for i in range(2, n+1):
    print(node[i])

'''
# 실패: 메모리 초과
# 노드의 개수 N (2 ≤ N ≤ 100,000)

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

node = [0] * (n+1)

def bfs():
    queue = deque([1])
    while queue:
        cur_node = queue.popleft()
        for i in range(2, n+1):
            if graph[cur_node][i] == 1 and node[i] == 0:
                node[i] = cur_node
                queue.append(i)

bfs()
for i in range(2,n+1):
    print(node[i])
'''
