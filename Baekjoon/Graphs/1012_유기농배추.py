# 실버 2, bfs로 풀이

from collections import deque 

def bfs(a,b):
    queue = deque([(a,b)])
    graph[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for kk in range(4):
            nx = x + dx[kk]
            ny = y + dy[kk]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

t = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(t):
    m, n, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1
    cnt = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(a,b)
                cnt += 1
    print(cnt)