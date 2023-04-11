import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
button = []
if m:
    button = list(input().split())

result = abs(100 - n)


for i in range(1000001):
    flag = False
    for ii in str(i):
        if ii in button:
            flag = True
            break
    if not flag:
        result = min(result, (len(str(i)) + abs(n-i)))

print(result)
