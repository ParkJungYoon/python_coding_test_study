import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
graph = [[int(i) for i in input().strip()] for _ in range(int(n))]
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)

def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append([nx,ny])

bfs(0,0)
print(graph[n-1][m-1])
