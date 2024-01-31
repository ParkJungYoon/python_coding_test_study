import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
dx, dy = (-2, -1, 1, 2, 2, 1, -1, -2), (1, 2, 2, 1, -1, -2, -2, -1)

def bfs(x,y):
    global graph
    queue = deque([(x,y,0)])
    graph[x][y] = 1
    while queue:
        x, y, jump = queue.popleft()
        if x == wish_x and y == wish_y:
            return jump
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx,ny,jump+1))


for _ in range(t):
    l = int(input())
    knight_x, knight_y = map(int, input().split())
    wish_x, wish_y = map(int, input().split())  
    graph = [[0] * l for _ in range(l)]

    result = bfs(knight_x, knight_y)
    print(result)