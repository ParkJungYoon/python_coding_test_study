import math
n, m = map(int, input().split())

answer = 1
for i in range(n,n-m,-1):
    answer *= i

answer = answer // math.factorial(m)
print(answer)