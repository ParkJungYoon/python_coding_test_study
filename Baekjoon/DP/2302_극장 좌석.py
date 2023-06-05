'''
vip 좌석 생기기 전
0, 1, 2, 3, 5
1,2 / 2, 1
1,2,3 / 2,1,3 / 1,3,2
1,2,3,4 / 2,1,3,4 / 2,1,4,3 / 1,2,4,3 / 1,3,2,4
'''

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [0] * (n+1)
dp[0], dp[1] = 1, 1

def fibo(num):
    if dp[num] != 0:
        return dp[num]
    dp[num] = fibo(num-1) + fibo(num-2)
    return dp[num]

fibo(n)
seat = list(range(1, n+1))
count = 1
vip = []
for i in range(m):
    fixed_seat = int(input().rstrip())
    vip.append(fixed_seat-1)

start = 0
for i in range(m):
    size = len(seat[start:vip[i]])
    cases = dp[size]
    count *= cases
    start = vip[i] + 1

size = len(seat[start:n])
cases = dp[size]
count *= cases

print(count)

'''
# 이유 모를.. spit으로는 안돼.ver

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [0] * (n+1)
dp[0], dp[1] = 1, 1

def fibo(num):
    if dp[num] != 0:
        return dp[num]
    dp[num] = fibo(num-1) + fibo(num-2)
    return dp[num]

fibo(n)
seat = ''.join(list(map(str, list(range(1, n+1)))))
count = 1

for i in range(m):
    fixed_seat = input().rstrip()
    temp = seat.split(fixed_seat)

    if not temp[0]:
        seat = temp[1]
    elif not temp[1]:
        seat = temp[0]
    else:
        cases = dp[len(temp[0])]
        count *= cases
        seat = temp[1]

if seat:
    cases = dp[len(seat)]
    count *= cases

print(count)

'''

'''
# 탑다운 참고자료
d = [0] * 100

def fibo(x):
    # 종료 조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
'''
