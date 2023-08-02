import sys
input = sys.stdin.readline

n = int(input())
dp = [10**9] * (n+1)
dp[0], dp[1] = 0, 0

energe = [(0,0)]

if n == 1:
    k = int(input())
    print(dp[n])
else:
    for _ in range(n-1):
        s, l = map(int, input().split())
        energe.append((s,l))

    k = int(input())

    dp[2] = dp[1] + energe[1][0]
    for i in range(3,n+1):
        # 현재 칸에서 1칸 전에서 뛰거나, 2칸 전에서 뛰거나
        dp[i] = min(dp[i-1] + energe[i-1][0], dp[i-2] + energe[i-2][1])

    # 매우 큰 점프는 1번만 사용할 수 있다는 반영해야함.
    # 위에 계산 중에 큰 점프 못하는 이유는 큰 점프 이후에 점프에서 값이 변해서
    current = dp[n]

    for i in range(4,n+1):
        big_jump_dp = dp[:]
        # 값을 바꿨으니깐 그 뒤로도 다 바뀜
        if dp[i-3] + k < dp[i]:
            big_jump_dp[i] = dp[i-3] + k
            for j in range(i+1,n+1):
                big_jump_dp[j] = min(dp[j], big_jump_dp[j-1] + energe[j-1][0], big_jump_dp[j-2] + energe[j-2][1])

            current = min(current, big_jump_dp[n])

    print(current)