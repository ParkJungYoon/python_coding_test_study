import sys
from collections import deque
input = sys.stdin.readline

r, c, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx, dy = (0,1,0,-1), (1,0,-1,0)

def find_bomb(graph):
    bomb = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O': 
                bomb.append((i,j))
    return bomb

def bfs():
    queue = deque(bomb)
    while queue:
        x, y = queue.popleft()
        graph[x][y] = "."
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                graph[nx][ny] = "."

bomb = find_bomb(graph)

time = 1
flag = True
while time != n:
    time += 1
    if flag:
        graph = [['O'] * c for _ in range(r)]
        flag = False
    else:
        bfs()
        bomb = find_bomb(graph)
        flag = True

for g in graph:
    print(''.join(g))