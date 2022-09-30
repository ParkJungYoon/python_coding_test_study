# 아이디어: type을 넘겨줘서 fires list에서 출발하면 +1, 아니면 -1
# m이 n을 넘어갈 때 어떻게 하지..? m 너무 큰데??? m 기준으로 반복 돌리면 안될거같아
# 미리 +몇을 할 지 체크해서 더해줄까?

# from queue import deque 
def solution(n, m, fires, ices):
    graph = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    dx, dy = (0,1,1,1,0,-1,-1,-1), (1,1,0,-1,-1,-1,0,1)

# n 이 [1,1] 이런 식으로 들어옴
def bfs(n, m, fires, ices, type):
    # queue = deque([n])
    x, y = n[0]-1, n[1]-1
    # 무조건 1초 이상 시간
    visited[x][y] = True

    # m번 반복
    for i in range(m):
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][y] = True