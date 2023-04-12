n = int(input())
nn = int(input())

graph = [[0] * n for _ in range(n)]

# 아래부터, 우, 상, 좌 방향으로 계속 돌기
dx, dy = (1,0,-1,0), (0,1,0,-1)
direction = 0
number = n ** 2

def move(x,y):
    global number, direction
    graph[x][y] = number
    nx, ny = x, y

    while True:
        number -= 1
        nx, ny = nx + dx[direction%4], ny + dy[direction%4]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            nx, ny = nx - dx[direction%4], ny - dy[direction%4]
            direction += 1
            number += 1
            continue
        if graph[nx][ny] != 0:
            nx, ny = nx - dx[direction%4], ny - dy[direction%4]
            direction += 1
            number += 1
            continue

        graph[nx][ny] = number

        if number == 1:
            break
    return

move(0,0)

for g in graph:
    print(*g)

for i in range(n):
    for j in range(n):
        if graph[i][j] == nn: print(i+1, j+1)

'''
(0,0) (1,0) (2,0) ... (4,0)
(4,1) (4,2) ... (4,4)
(3,4) (2,4) (1,4) (0,4)
(0,3) (0,2) (0,1)

아래 방향으로 쭉 내려가다가 1)범위를 벗어난다. 2)이미 방문한 그래프다.
하면 방향을 틀어서 쭉 간다.
'''