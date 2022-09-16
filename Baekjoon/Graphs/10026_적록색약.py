from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
dx, dy = (0,1,0,-1), (1,0,-1,0)


def bfs(i,j):
    queue = deque([(i,j)])
    cur = graph[i][j]

    if cur == 'B':
        graph[i][j] = 0
    else: graph[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and cur == graph[nx][ny]:
                if cur == 'B':
                    graph[nx][ny] = 0
                else: graph[nx][ny] = 1
                queue.append((nx,ny))

# 적록색약 bfs
def bfs_RG(i,j):
    queue = deque([(i,j)])
    cur = graph[i][j]
    graph[i][j] = 2

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and cur == graph[nx][ny]:
                graph[nx][ny] = 2
                queue.append((nx,ny))


cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] in ["B","R","G"]:
            cnt += 1
            bfs(i,j)

# 적록색약 bfs
cnt2 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] in [0,1]:
            cnt2 += 1
            bfs_RG(i,j)

print(cnt, cnt2)


# if cur == 'B':
    #     graph[i][j] = 0
    # else: graph[i][j] = 1

# def bfs(i,j):
#     queue = deque([(i,j)])
#     cur = graph[i][j]
#     graph[i][j] = 1

#     while queue:
#         x, y = queue.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < n and cur == graph[nx][ny]:
#                 graph[nx][ny] = 1
#                 queue.append((nx,ny))
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] != 1:
#             cnt += 1
#             bfs(i,j)

# print(cnt)