n = int(input())
a = list(map(int, input().split()))

dp = a[:]

# i가 증가하면서 그 범위까지 중 증가하는 경우에 더한 값과 지금 dp[i]에 저장하고
# 있는 값을 비교해서 큰 값으로 업데이트 해준다.
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+a[i])

print(max(dp))