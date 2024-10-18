'''
X0X
X00X

dp[3]일 때, dp[1] + dp[3] or
6, 10, 13, 9, 8, 1  
6, 16, max(19, 16, 10 + 13)
'''
import sys
input = sys.stdin.readline

n = int(input())
fruit = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = fruit[0]
if n > 1:
    dp[1] = fruit[0] + fruit[1]
if n > 2:
    # 바로 직전의 dp값, 전전 dp값 + 현재 값
    dp[2] = max(dp[1], dp[0]+fruit[2], fruit[1]+ fruit[2])


for i in range(3,n):
    # 바로 직전의 dp값, 전전 dp 값 + 현재값, 전전전dp값 + 전값 + 현재값
    dp[i] = max(dp[i-1], dp[i-2]+fruit[i], fruit[i-1]+fruit[i]+dp[i-3])


print(dp[-1])