import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dx, dy = (0,1,0,-1), (1,0,-1,0)
time = 0
total_cheeze = 0

def bfs(x,y):
    visited = [[False] * c for _ in range(r)]

    queue = deque([])
    cheeze = deque([])
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 1:
                    cheeze.append((nx,ny))
                    visited[nx][ny] = True

    # 치즈 녹은 자리 0으로 한 번에 바꿔주기
    cheeze_count = len(cheeze)

    while cheeze:
        x, y = cheeze.popleft()
        graph[x][y] = 0

    return cheeze_count

temp = []
while True:
    total_cheeze = bfs(0,0)
    temp.append(total_cheeze)

    if total_cheeze == 0:
        break

    time += 1

print(time)
print(temp[-2])