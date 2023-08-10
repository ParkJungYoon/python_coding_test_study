import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = (0,1,1,1,0,-1,-1,-1), (1,1,0,-1,-1,-1,0,1)

def bfs(x,y):
    queue = deque([(x,y,1)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    while queue:
        x, y, count = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    return count
                elif graph[nx][ny] == 0:
                    queue.append((nx,ny,count+1))
                    visited[nx][ny] = True

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 1:
            answer = max(answer, bfs(i,j))

print(answer)

'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
queue = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))
    
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j, 1))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
answer = 0
while queue:
    x, y, d = queue.popleft()
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = d + 1
                queue.append((nx, ny, d + 1))

for i in range(n):
    answer = max(answer, *graph[i])
print(answer - 1)
'''