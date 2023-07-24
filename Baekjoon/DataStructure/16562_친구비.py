'''
같은 무리인 친구를 서로소 집합으로 모음.
이제 한 무리당 최소 비용인 친구 한 명씩만 사귀면 준석이는 친구를 사귈 수 있다.
'''

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
cost = list(map(int, input().split()))
parents = [i for i in range(n+1)]

def find_parent(n):
    if parents[n] != n:
        parents[n] = find_parent(parents[n])
    return parents[n]

def union_parents(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if cost[a-1] < cost[b-1]:
        parents[b] = a
    else:
        parents[a] = b

for i in range(m):
    v, w = map(int, input().split())
    union_parents(v,w)

total_cost = 0
for i in range(1, n+1):
    if i == parents[i]:
        total_cost += cost[i-1]

if total_cost <= k:
    print(total_cost)
else:
    print("Oh no")

'''
반례

5 3 20
20 30 10 20 10
1 3
2 4
5 4

5 5 100
10 20 30 40 50
1 2
3 4
2 3
4 5
5 1

정답: 10
'''