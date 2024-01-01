import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

def bfs(x, y, dep):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and graph[nx][ny] > dep:
                visited[nx][ny] = True
                queue.append((nx,ny))


max_num = max([max(g) for g in graph])
result = 0
for dep in range(0, max_num):
    temp = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > dep and visited[i][j] == False:
                bfs(i,j,dep)
                temp += 1
    result = max(result, temp)

print(result)

'''
강수량이 0이면 아무 지역도 물에 잠기지 않을 수도 있다.
'''