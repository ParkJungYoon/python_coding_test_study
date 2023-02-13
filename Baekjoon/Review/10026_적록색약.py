import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[i for i in input().rstrip()] for _ in range(n)]
dx, dy = (1,0,-1,0), (0,-1,0,1)

# 적록색약이면 빨강R == 초록G
color_weakness = False
def bfs(x,y):
    queue = deque([(x,y)])
    cur = graph[x][y]
    graph[x][y] = "W"
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if color_weakness:
                if cur in ("R", "G"):
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] in ("R", "G"):
                        queue.append((nx,ny))
                        graph[nx][ny] = "W"
                else:
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == cur:
                        queue.append((nx,ny))
                        graph[nx][ny] = "W"
            else:    
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == cur:
                    queue.append((nx,ny))
                    graph[nx][ny] = "W"

count1 = 0
count2 = 0
color_weakness_graph = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if graph[i][j] != "W":
            bfs(i,j)
            count1 += 1

graph = color_weakness_graph
color_weakness = True
for i in range(n):
    for j in range(n):
        if graph[i][j] != "W":
            bfs(i,j)
            count2 += 1

print(count1, count2)