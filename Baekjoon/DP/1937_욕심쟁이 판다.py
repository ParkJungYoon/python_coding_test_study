import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
dx, dy = (0,1,0,-1), (1,0,-1,0)

forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def dfs(x,y):
    if dp[x][y]: return dp[x][y]
    dp[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx,ny) + 1)
    return dp[x][y]

max_num = 0
for i in range(n):
    for j in range(n):
        max_num = max(max_num, dfs(i,j))

print(max_num)


'''
dfs + dp
아이디어 노트
- 모든 지점에서 돌려봄
- 조건: 방문하지 않음. 자신보다 수가 큰 지점.
'''