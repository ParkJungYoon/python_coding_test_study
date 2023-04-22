'''
상근: SK, 창영: CY
상근이가 시작
돌은 1개 or 3개
'''

n = int(input())
if n % 2 == 0:
    print('CY')
else:
    print('SK')


'''
# 매모리 초과 시간 초과 파티 ㅎ..
from collections import deque
n = int(input())

dp = [-1] * (n+1)
playground = deque([0])

# 1 상그닝, -1 창영
while playground:
    turn = playground.popleft()
    if turn == n: break

    for i in (turn+1, turn+3):
        if i <= n:
            dp[i] = dp[turn] * (-1)
            playground.append(i)


# # -1은 상그닝, 1은 창영
# playground = deque([(0,1)])

# while playground:
#     turn, player = playground.popleft()
#     if turn == n: break

#     for i in (turn+1, turn+3):
#         if i <= n:
#             playground.append((i, player*(-1)))


if dp[n] == 1:
    print("SK")
else:
    print("CY")
'''