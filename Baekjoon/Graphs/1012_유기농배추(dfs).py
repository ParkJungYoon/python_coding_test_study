# 실버 2, dfs로 풀이

# sys.setrecursionlimit(10000) 를 입력하지 않으면 런타임 오류가 발생한다.
# 파이썬의 기본 재귀 한도는 1000이고, 재귀 깊이가 1000을 넘어갈 경우 모듈을 추가해야 한다.

import sys
sys.setrecursionlimit(10000)

t = int(input())

def dfs(i,j):
    for ii in range(len(dx)):
        y = i + dy[ii]
        x = j + dx[ii]
        if y >= 0 and y < n and x >= 0 and x < m and graph[y][x] == 1:
            graph[y][x] = 0
            dfs(y,x)


for _ in range(t):
    count = 0
    m, n, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for _ in range(k):
        nx, ny = map(int,input().split())
        graph[ny][nx] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                graph[i][j] = 0
                dfs(i,j)
                count += 1
    print(count)