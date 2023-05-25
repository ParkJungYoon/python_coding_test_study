import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
dict_str = defaultdict(int)
count = 0

for _ in range(n):
    temp = input().rstrip()
    dict_str[temp] = 1

for _ in range(m):
    temp2 = input().rstrip()
    if dict_str[temp2] == 1:
        count += 1

print(count)