'''
단순 구현 방법
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [[0] * 20 for _ in range(n)]
for _ in range(m):
    temp = list(map(int, input().split()))

    if len(temp) == 3:
        command, idx, seat_num = temp[0], temp[1], temp[2]
    else:
        command, idx = temp[0], temp[1]

    if command == 1:
        train[idx-1][seat_num-1] = 1
        print(train)
    elif command == 2:
        train[idx-1][seat_num-1] = 0
    # 뒤로 갈 때는 뒤에 인덱스부터 업데이트
    elif command == 3:
        print(idx)
        for i in range(19,-1,-1):
            if train[idx-1][i] == 1:
                if i == 19:
                    train[idx-1][i] = 0
                else:
                    train[idx-1][i] = 0
                    train[idx-1][i+1] = 1
    elif command == 4:
        for i in range(20):
            if train[idx-1][i] == 1:
                if i == 0:
                    train[idx-1][i] = 0
                else:
                    train[idx-1][i] = 0
                    train[idx-1][i-1] = 1

answer = []
for t in train:
    if t not in answer:
        answer.append(t)
print(len(answer))


'''
# 비트마스킹 풀이
# https://ip99202.github.io/posts/%EB%B0%B1%EC%A4%80-15787-%EA%B8%B0%EC%B0%A8%EA%B0%80-%EC%96%B4%EB%91%A0%EC%9D%84-%ED%97%A4%EC%B9%98%EA%B3%A0-%EC%9D%80%ED%95%98%EC%88%98%EB%A5%BC/

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [0]*n
print(bin(1 << 20))
print(bin(2**20))
# 이때 오른쪽부터 자리 배치를 하여 3210 순으로 배치가 됨.
for _ in range(m):
    op = list(map(int, input().split()))

    if op[0] == 1:
        i, x = op[1] - 1, op[2] - 1
        train[i] = train[i] | 1 << x # '|' : bit 단위로 or연산
        # << (Binary left Shift) : bit 단위로 왼쪽으로 비트단위 밀기 연산을 합니다. ('|' 보다 연산자 우선순위가 높음.)
        # n << m : n * 2의 m승
        # 즉 2진수에 맞게 x 자리에 1이되고 나머지는 0.

    elif op[0] == 2:
        i, x = op[1] - 1, op[2] - 1
        train[i] = train[i] & ~(1 << x)
        # ~ : 비트 NOT 연산
        # ~(1 << x) 을 통해서 x자리만 0이 되고 나머지는 1
        # 이를 통해서 train[i]는 유지하되 x자리는 AND 연산자로 0이 되어 하차

    elif op[0] == 3:
        i = op[1] - 1
        train[i] = train[i] << 1
        train[i] = train[i] & ~(1 << 20)
        # train[i] << 1 을 통해서 왼쪽으로 비트단위 밀기 연산
        # 0011 -> 0110
        # 1000 -> ~(1000) -> 0111 : AND 연산을 하여 맨 앞자리를 비워준다.

    elif op[0] == 4:
        i = op[1] - 1
        train[i] = train[i] >> 1
        # train[i] >> 1 을 통해서 오른쪽으로 비트단위 밀기 연산
        # 0100 -> 0010

print(len(set(train)))
'''