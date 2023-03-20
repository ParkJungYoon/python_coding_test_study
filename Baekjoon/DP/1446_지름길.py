n, d = map(int, input().split())

dp = [i for i in range(d+1)]

shortcut = []
for _ in range(n):
    start, end, distance = map(int, input().split())
    shortcut.append((start, end, distance))

for i in range(d+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1]+1)
    for start, end, distance in shortcut:
        if i == start and end <= d and dp[i] + distance < dp[end]:
            dp[end] = dp[i] + distance

print(dp[d])

'''
간단한 예시
[0,1,2,3,4,5,6,7,8]
0 -> 4 : 2
6 -> 8 : 1

i=0 [0,1,2,3,2,5,6,7,8]
i=1 [0,1,2,3,2,5,6,7,8]
i=2 [0,1,2,3,2,5,6,7,8]
...
i=5 [0,1,2,3,2,3,6,7,8]
i=6 [0,1,2,3,2,3,4,7,5]
i=7 [0,1,2,3,2,3,4,5,5]
i=8 [0,1,2,3,2,3,4,5,5]
'''