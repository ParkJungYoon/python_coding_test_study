import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dict = defaultdict(int)
result = []

for _ in range(n):
    person, log = input().split()
    if log == "enter":
        dict[person] = 1
    elif log == "leave":
        dict[person] = 0

for person, check in dict.items():
    if check != 0:
        result.append(person)

result.sort(reverse=True)

for p in result:
    print(p)