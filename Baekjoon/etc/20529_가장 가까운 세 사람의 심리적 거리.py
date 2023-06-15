import sys
from itertools import combinations
input = sys.stdin.readline

t = int(input())

def distance(a,b):
    count = 0
    for i in range(4):
        if a[i] != b[i]:
            count += 1
    return count

for _ in range(t):
    n = int(input())
    friends = list(input().split())
    if n >= 33:
        print(0)
        continue
    result = 10**9
    for combi in list(combinations(friends, 3)):
        temp = 0
        temp += distance(combi[0], combi[1])
        temp += distance(combi[0], combi[2])
        temp += distance(combi[1], combi[2])
        result = min(result, temp)
    print(result)

'''
3
3
ENTJ INTP ESFJ
4
ESFP ESFP ESFP ESFP
5
INFP INFP ESTP ESTJ ISTJ
'''