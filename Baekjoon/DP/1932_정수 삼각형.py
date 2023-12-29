import sys
import copy
input = sys.stdin.readline

n = int(input())

dp = [0] * n
dp[0] = int(input())
temp = copy.deepcopy(dp)

for _ in range(1, n):
    floor = list(map(int, input().split()))

    for i in range(len(floor)):
        if i == 0:
            dp[i] += floor[i]
        elif i == (len(floor)-1):
            dp[i] = temp[i-1] + floor[i]
        else:
            dp[i] = max(temp[i-1], temp[i]) + floor[i]

    temp = copy.deepcopy(dp)

print(max(dp))


'''
7
10 15
18 16 15
20 25 20 19
24 30 25 26 24

풀이 아이디어
가능한 경우에서 최대로 누적하면서 dp에 저장하기
'''