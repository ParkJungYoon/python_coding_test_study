import sys
sys.setrecursionlimit(int(1e5))
LOG = 21

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

d = [0] * (n+1)
parent = [[0] * LOG for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node, deep):
    visited[node] = True
    d[node] = deep

    for cur in graph[node]:
        if not visited[cur]:
            parent[cur][0] = node
            dfs(cur, deep+1)

# 전체 부모 관계 설정
def set_parent():
    dfs(1,0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            print(i, j)
            print(parent[j][i-1])
            parent[j][i] = parent[parent[j][i-1]][i-1]


# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a;
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))


'''
# 시간 초과

import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

d = [0] * (n+1)
parent = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node, deep):
    visited[node] = True
    d[node] = deep

    for cur in graph[node]:
        if not visited[cur]:
            parent[cur] = node
            dfs(cur, deep+1)

dfs(1,0)

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(lca(x,y))

'''