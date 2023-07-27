import sys
input = sys.stdin.readline

def dfs(x, y, goguma, cur_time):
    global max_goguma

    if t == cur_time:
        max_goguma = max(max_goguma, goguma)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] == ".":
                dfs(nx, ny, goguma, cur_time+1)
            elif graph[nx][ny] == "S":
                graph[nx][ny] = "."
                dfs(nx, ny, goguma+1, cur_time+1)
                graph[nx][ny] = "S"


r, c, t = map(int, input().split())
gahee_x, gahee_y = 0, 0
graph = []

dx, dy = (0,1,0,-1), (1,0,-1,0)
max_goguma = 0

for rr in range(r):
    temp = []
    one_map = input().rstrip()
    for cc in range(c):
        if one_map[cc] == "G": gahee_x, gahee_y = rr, cc
        temp.append(one_map[cc])
    graph.append(temp)

# 가희 위치로도 이동 가능할 수 있게 해야함 (이거 안해서 70퍼쯤에서 틀림)
graph[gahee_x][gahee_y] = "."

dfs(gahee_x, gahee_y, 0, 0)
print(max_goguma)
