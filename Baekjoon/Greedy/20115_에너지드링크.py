import sys
input = sys.stdin.readline

n = int(input())
drink = list(map(int, input().split()))

last = max(drink)

print((sum(drink) - last) / 2 + last)