import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for check in a:
    remain = check - b
    if remain <= 0: answer += 1
    else: answer += 1 + math.ceil(remain / c)

print(answer)