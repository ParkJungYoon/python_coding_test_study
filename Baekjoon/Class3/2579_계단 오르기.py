n = int(input())
score = [0]
for _ in range(n): score.append(int(input()))

d = [0] * 301

if len(score) <= 3:
    print(sum(score))
else:
    d[1] = score[1]
    d[2] = score[1] + score[2]

    for i in range(3, n+1):
        d[i] = max(score[i] + d[i-2], score[i] + score[i-1] + d[i-3])

    print(d[n])

'''
# 괜히 복잡하게 생각함
n = int(input())
score = [0]
for _ in range(n): score.append(int(input()))

print(score)

d = [[0,0] for _ in range(301)]

d[1][0], d[1][1] = score[1], 1
# if score[1] > score[2]:
#     d[2][0], d[2][1] = score[2]+score[1], 2
# else:
#     d[2][0], d[2][1] = score[2], 1

# 1을 안밟고 바로 가는게 더 크면
if max(score[2]+score[3], score[2]+score[4]) > score[1]+score[2]+score[4]:
    d[2][0], d[2][1] = score[2], 1
else:
    d[2][0], d[2][1] = score[2]+score[1], 2

for i in range(3, n+1):
    if score[i] + d[i-1][0] > score[i] + d[i-2][0] and d[i-1][1] < 2:
        d[i][0] = score[i] + d[i-1][0]
        d[i][1] = d[i-1][1] + 1
    else:
        d[i][0] = score[i] + d[i-2][0]
        d[i][1] = 1
    print(d[:n+1])

print(d[n][0])
'''

'''
반례 

3  d
10 10
20 30
100 130

output : 110
answer : 120

첫계단 밟지 않고 건너 뛰어 20 + 100
'''