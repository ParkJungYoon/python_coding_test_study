import sys
input = sys.stdin.readline
n = int(input())
road = list(map(int,input().split()))
price = list(map(int,input().split()))

now = price[0]
cost = 0
for i in range(1,n):
    if now > price[i]:
        cost += now * road[i-1]
        now = price[i]
    else:
        cost += now * road[i-1]
print(cost)