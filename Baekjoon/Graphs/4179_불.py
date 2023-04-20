'''
지훈이 위치, 불이 붙은 위치
-> 탈출 가능 여부, 얼마나 걸릴지
메모리 초과 지옥 ㅎㅎ..

https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-4179-%EB%B6%88-BFS
'''
import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
miro = []
queue = deque([])
dx, dy = (0,1,0,-1), (1,0,-1,0)
answer = "IMPOSSIBLE"

# 큐에 1번에 -1이면 불! 1이상은 지훈이!
# 지훈이가 큐에 먼저 들어가야 함.
for i in range(r):
    miro.append(list(input().rstrip()))
    for t in range(c):
        if miro[i][t] == "J": queue.append((1,i,t))
for i in range(r):
    for t in range(c):
        if miro[i][t] == "F": queue.append((-1,i,t))

def bfs():
    global answer

    while queue:
        check, x, y = queue.popleft()
        if check > 0 and (x == 0 or x == (r-1) or y == 0 or y == (c-1)):
            answer = check
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and miro[nx][ny] != "#":
                if check >= 1 and miro[nx][ny] == ".":
                    queue.append((check+1,nx,ny))
                    miro[x][y] = "_"

                elif check == -1 and miro[nx][ny] != "F":
                    queue.append((check,nx,ny))
                    miro[nx][ny] = "F"

bfs()
print(answer)