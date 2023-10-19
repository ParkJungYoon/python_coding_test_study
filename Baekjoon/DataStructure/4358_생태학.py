import sys
input = sys.stdin.readline
from collections import defaultdict

count = 0
dict = defaultdict(int)
while True:
    tree = input().rstrip()

    if not tree:
        break

    count += 1
    dict[tree] += 1

sorted_key = sorted(list(dict.keys()))
for key in sorted_key:
    # print(key, round((dict[key] / count) * 100, 4))
    print('%s %.4f'%(key, (dict[key] / count) * 100))
