import sys
input = sys.stdin.readline
n = int(input())
p = []
p.append(0)
for i in range(n):
    p.append(int(input()))
p.append(0)

for i in range(1,n+1):
    if p[i-1] <= p[i] and p[i] >= p[i+1]:
            print(i)