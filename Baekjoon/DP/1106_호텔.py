import sys
input = sys.stdin.readline

# 비용, 고객 수
# dp 인덱스가 고객 수, 값이 비용
c, n = map(int, input().split())
dp = [10**9 for _ in range(c+100)]
dp[0] = 0
cost_list = [list(map(int,input().split())) for _ in range(n)]

# for _ in range(n):
#     cost, customer = map(int, input().split())
#     dp[customer] = cost
#     cost_list.append((cost, customer))

for cost, customer in cost_list:
    for idx in range(customer, c+100):
        dp[idx] = min(dp[idx], dp[idx-customer] + cost)

print(min(dp[c:]))


'''
[배낭 알고리즘] -> 대표적인 DP 문제
n개의 물건과 배낭이 있을 때, 각 물건에는 가치와 무게가 존재한다.
또한 각 물건은 1개씩만 있다. 배낭에는 담을 수 있는 최대 용량이 존재한다.
이런 조건일 때, 배낭의 최대 용량을 초과하지 않으면서 배낭에 담을 수 있는 최대 가치의 합을 찾는 문제이다.
https://howudong.tistory.com/106
'''