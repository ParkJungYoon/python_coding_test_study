import sys
input = sys.stdin.readline
from math import factorial

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    result = factorial(m) // (factorial(m-n) * factorial(n))
    print(result)
