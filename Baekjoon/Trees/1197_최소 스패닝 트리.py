import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
edges = []
result = 0

parent = [i for i in range(v+1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 부모가 같다는건 이미 연결되어 있다는거임! 다를 때만 union 연산
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)