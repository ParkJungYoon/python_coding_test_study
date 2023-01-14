import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = False
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i]:
                queue.append(i)
                visited[i] = False

dfs(v)
print()
bfs(v)