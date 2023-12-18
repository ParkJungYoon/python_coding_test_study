import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for i in range(x1, x2):
            graph[j][i] = 1

def bfs(x, y):
    count = 0
    queue = deque([(x,y)])
    graph[y][x] = 1
    count += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                count += 1
                queue.append((nx,ny))
    return count

result = []
for i in range(n):
    for j in range(m):
        if graph[j][i] == 0:
            count = bfs(i, j) 
            result.append(count)

result.sort()

print(len(result))
print(*result)