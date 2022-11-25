from sys import stdin
from collections import deque
input = stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] 

def bfs():
    queue = deque()
    # 2일 때 큐에 넣음
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx,ny))


print(graph)