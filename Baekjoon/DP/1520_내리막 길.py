import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx, dy = (1,0,-1,0), (0,-1,0,1)

# x, y에서 목적지까지 가는 경로가 몇 개인지 dp[x][y]에 기록
def dfs(x,y):
    # 목적지까지 도착하면 한 개의 경로
    if x == (m-1) and y == (n-1):
        return 1
    # 기존에 x, y를 방문한 적이 있다면 그대로 dp 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx,ny)

    return dp[x][y]

print(dfs(0,0))


'''
50 45
46 40

그냥 dfs만 쓰면 시간초과 난다.
dfs + dp 사용해야할거 같다.
https://simsimjae.tistory.com/20
- dfs는 50*50 2차원 배열에서도 시간초과 확률이 높다.
- 그래서 최대한 중복 연산을 피해야 한다. (dp를 활용해서)
- (0,0)에서 (4,4)를 거쳐 (50,50)으로 가는 경로가 있다면 (4,4)까지 가는 경로의 수를 미리 계산해둔다면 중복 계산을 피할 수 있다.
'''