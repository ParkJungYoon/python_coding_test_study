import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]

dx, dy = (1,0,0,-1), (0,1,-1,0)

def dfs(x,y):
    if x == (m-1) and y == (n-1):
        return 1 

    # 한 번도 방문한 적 없는 경우에만 dfs 돌림
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
                dp[x][y] += dfs(nx,ny)

    return dp[x][y]

print(dfs(0,0))
