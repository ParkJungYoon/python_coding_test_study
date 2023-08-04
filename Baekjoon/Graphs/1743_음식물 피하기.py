import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    count = 1
    queue = deque([(x,y)])
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                count += 1
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return count


n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
dx, dy = (0,1,0,-1), (1,0,-1,0)

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer = max(answer, bfs(i,j))

print(answer)