import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

temp = 0
prefix_sum = [0]
for number in numbers:
    temp += number
    prefix_sum.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j]-prefix_sum[i-1])