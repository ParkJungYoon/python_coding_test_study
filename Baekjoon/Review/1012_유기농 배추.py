import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dx, dy = (1,0,-1,0), (0,-1,0,1)

def bfs(x,y):
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx,ny))


for _ in range(t):
    count = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                bfs(i,j)
                count += 1
    
    print(count)

    