import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (1,0,-1,0), (0,-1,0,1)
queue = deque([])
result = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx,ny))

bfs()

for ii in range(n):
    for jj in range(m):
        if box[ii][jj] == 0:
            print(-1)
            exit(0)
    result = max(result, max(box[ii]))

print(result-1)
