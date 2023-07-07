import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    check = list(map(int, input().split()))
    status = defaultdict(int)
    half = check[0] // 2
    flag = False

    for i in check[1:]:
        status[i] += 1
        if status[i] > half:
            print(i)
            flag = True
            break

    if not flag: print("SYJKGW")