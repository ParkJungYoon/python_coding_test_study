import sys
input = sys.stdin.readline
k = int(input())
money = []

for i in range(k):
    num = int(input())
    if num == 0:
        money.pop()
    else:
        money.append(num)
if len(money) == 0: print(0)
else: print(sum(money))