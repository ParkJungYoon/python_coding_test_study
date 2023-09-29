import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    check_list = defaultdict(int)
    for nn in note1:
        check_list[nn] = 1

    for nnn in note2:
        print(check_list[nnn])

'''
반례

2
5
1 2 3 4 5
5
3 4 5 6 7
5
3 4 5 6 7
5
1 2 3 4 5
'''