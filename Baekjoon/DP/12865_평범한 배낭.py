import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * (n+1) for _ in range(k+1)]

'''
배낭 최대 무게  배낭 (무게w, 가치v)
    0      1(6,13) 2(4,8) 3(3,6) 4(5,12)
    1        0       0       0
    2        0       0       0
    3        0       0       6
    4        0       8    max(8,6+0)
    5        0       8    max(8,6+0)
    6        13  max(13,8+0)  max(13,6+0)
    7        13  max(13,8+0)  max(13,6+8)
내 물건을 배낭에 담거나, 안 담거나 두 가지 경우
1. 첫번째 배낭은 무조건 담는 경우밖에 없음.
'''

# i는 물품 번호 (1~n번까지)
for i in range(1, n+1):
    w, v = map(int, input().split())

    # j는 무게 (k가 최대 공간, 내가 3만큼 넣으면 남은 공간은 4)
    for j in range(k+1):
        # 현재 배낭의 최대 무게는 j이다.
        # j-w가 남은 배낭의 공간
        if w > j:
            dp[j][i] = dp[j][i-1]
        else:
            dp[j][i] = max(dp[j][i-1], v + dp[j-w][i-1])

    '''
    틀린 이유: 물건의 크기가 배낭의 크기보다 큰 경우는 그냥 넘어가서 틀림.
    왜냐하면 다음 인덱스 검색 때 그 직전의 값을 기준으로 맥스멈 값을 계산하는데
    그 앞 단 인덱스를 계산 안하고 넘어가면 0이기 때문에!
    '''
    # j는 무게 (k가 최대 공간, 내가 3만큼 넣으면 남은 공간은 4)
    # if w > k:
    #     for jj in range(1,k+1):
    #         dp[jj][i] = dp[jj][i-1]
    # for j in range(w, k+1):
    #     # 현재 배낭의 최대 무게는 j이다.
    #     # j-w가 남은 배낭의 공간
    #     dp[j][i] = max(dp[j][i-1], v + dp[j-w][i-1])

print(dp[-1][-1])


    # # 1. 바로 앞이랑 지금이랑 비교해서 무게가 안넘는 기준에서 더 가치 큰거
    # # 2. 앞이랑 지금이랑 더해서 큰거
    # if w >= k:
    #     dp[i] = [dp[i-1][0], dp[i-1][1]]
    #     continue

    # if dp[i-1][0] + w <= k:
    #     temp_w, temp_v = dp[i-1][0] + w, dp[i-1][1] + v
    # elif dp[i-1][1] >= v:

        