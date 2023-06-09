'''
공기청정기는 1열에만, 그리고 두 칸을 차지함.

1. 확산
- 공기청정기 없는 곳으로 확산
- 확산되는 양 : Ar,c//5
- 남은 미세먼지 양 : Ar,c - (Ar,c/5)x(확산된 방향의 개수)

2. 공기청정기 작동
- 위쪽 : 반시계 방향으로 순환
- 아래쪽 : 시계 방향으로 순환
'''

import sys
from collections import deque
input = sys.stdin.readline

# r,c가 안커서
def find_dust():
    dust = deque([])
    for rr in range(r):
        for cc in range(c):
            if graph[rr][cc] != 0 and graph[rr][cc] != -1:
                dust.append((rr,cc))
    return dust

# 1초 확산
# 동시에 확산되어야 한다. 그냥 바로 값을 더하고 업데이트 해주니깐 문제가 생김.
def diffusion(dust):
    temp = [[0] * c for _ in range(r)]
    while dust:
        x, y = dust.popleft()
        amount = graph[x][y] // 5
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                temp[nx][ny] += amount
                graph[x][y] -= amount
    
    for i in range(r):
        for j in range(c):
            graph[i][j] += temp[i][j]


def air_cleaner_counterclockwise(air_cleaner):
    x, y = air_cleaner
    # 좌, 상, 우, 하 (반시계 방향)
    dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)
    direction = 0
    before = 0
    while True:
        nx, ny = x + dx[direction], y + dy[direction]
        if nx == air_cleaner[0] and ny == air_cleaner[1]:
            break
        if nx < 0 or ny < 0 or ny >= c:
            nx, ny = x - dx[direction], y - dy[direction]
            direction += 1
            continue
        temp = graph[nx][ny]
        graph[nx][ny] = before
        before = temp
        x, y = nx, ny

def air_cleaner_clockwise(air_cleaner):
    x, y = air_cleaner
    # 좌, 하, 우, 상 (시계 방향)
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    direction = 0
    before = 0
    while True:
        nx, ny = x + dx[direction], y + dy[direction]
        if nx == air_cleaner[0] and ny == air_cleaner[1]:
            break
        if nx >= r or ny < 0 or ny >= c:
            nx, ny = x - dx[direction], y - dy[direction]
            direction += 1
            continue
        temp = graph[nx][ny]
        graph[nx][ny] = before
        before = temp
        x, y = nx, ny

r, c, t = map(int, input().split())
graph = []
machine = []
dx, dy = (0,-1,0,1), (1,0,-1,0)

for i in range(r):
    temp = list(map(int, input().split()))
    for j in range(c):
        if temp[j] == -1:
            machine.append((i,j))
    graph.append(temp)

# 회전할 때 모서리 (공기청정기 위치 빼고)
# top_edges = [(0,0),(machine[0][0],c-1), (0,c-1)]
# bottom_edges = [(machine[1][0],c-1), (r-1,c-1), (r-1,0)]

for tt in range(t):
    dust = find_dust()
    diffusion(dust)
    air_cleaner_counterclockwise(machine[0])
    air_cleaner_clockwise(machine[1])

final_dust = find_dust()
result = 0
while final_dust:
    temp = final_dust.popleft()
    result += graph[temp[0]][temp[1]]

print(result)

'''
[ 처음 확산 생각 ]
1)
- 먼지의 좌표를 가지고 있고, bfs로 확산하면서 그 좌표를 새로 가지고 있다가 dust를 덮어줘야겠다.
라고 생각함.
- 근데 다시 보니 공기청정기 때문에 좌표가 변경됨.

2) 확산될 때 바로 값을 더해주면, 그 위치에 값이 변경되어서 확산 양이 달라짐.
더해줘야하는걸 temp 해줬다가 마지막에 +=

[ 처음 회전 코드 ]

- 모서리 가지고 있고 나머지 하나씩 돌리는걸 생각함.
- 범위 헷갈려서 미춰버륄뻔... 다른 방법 찾음 ㅠ

def air_cleaner_counterclockwise(air_cleaner):
    x, y = air_cleaner
    e1, e2, e3, e4 = graph[top_edges[0][0]][top_edges[0][1]], 0, graph[top_edges[1][0]][top_edges[1][1]], graph[top_edges[2][0]][top_edges[2][1]]
    print(e1,e2,e3,e4)
    for bottom in range(c-1,1,-1):
        graph[x][bottom] = graph[x][bottom-1]
    for right in range(0,x-1):
        graph[right][c-1] = graph[right+1][c-1]
    for top in range(0,c-1):
        graph[0][top] = graph[0][top+1]
    for left in range(x-1,0,-1):
        graph[left][0] = graph[left-1][0]

    graph[top_edges[0][0]+1][top_edges[0][1]] = e1
    graph[x][y+1] = e2
    graph[top_edges[1][0]-1][top_edges[1][1]] = e3
    graph[top_edges[2][0]][top_edges[2][1]-1] = e4


def air_cleaner_clockwise(air_cleaner):
    x, y = air_cleaner
    e1, e2, e3, e4 = 0, graph[bottom_edges[0][0]][bottom_edges[0][1]], graph[bottom_edges[1][0]][bottom_edges[1][1]], graph[bottom_edges[2][0]][bottom_edges[2][1]]
    print(e1,e2,e3,e4)
    for top in range(c-1,1,-1):
        graph[x][top] = graph[x][top-1]
    for right in range(r-1,x,-1):
        graph[right][c-1] = graph[right-1][c-1]
    for bottom in range(0,c-1):
        graph[r-1][bottom] = graph[r-1][bottom+1]
    for left in range(x,r-2):
        graph[left][0] = graph[left+1][0]

    graph[x][y+1] = e1
    graph[bottom_edges[0][0]+1][bottom_edges[0][1]] = e2
    graph[bottom_edges[1][0]][bottom_edges[1][1]-1] = e3
    graph[bottom_edges[2][0]-1][bottom_edges[2][1]] = e4
'''