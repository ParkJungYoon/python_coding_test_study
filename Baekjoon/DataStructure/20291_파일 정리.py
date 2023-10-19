import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    name, extension = input().strip().split(".")
    dic[extension] += 1
    print(extension)

result = sorted(list(dic.keys()))

for r in result:
    print(r, dic[r])
