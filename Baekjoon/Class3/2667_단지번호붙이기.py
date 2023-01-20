import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[int(i) for i in input().rstrip()] for _ in range(n)]
dx, dy = (1,0,-1,0), (0,-1,0,1)
result = []

def bfs(x,y):
    count = 0
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    if count == 0: count += 1
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i,j))

result.sort()
print(len(result))
print(*result, sep = "\n")

'''
반례
5
00000
00001
00000
01000
11011
'''