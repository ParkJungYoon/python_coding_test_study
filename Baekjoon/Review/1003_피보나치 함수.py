t = int(input())
dp = [(0,0)] * 41

dp[0] = (1,0)
dp[1] = (0,1)

def fibo(n):
    if n <= 1: return dp[n]
    for i in range(2, n+1):
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    return dp[n]

for _ in range(t):
    print(*fibo(int(input())))