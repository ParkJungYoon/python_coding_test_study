import sys
# 재귀 깊이 제한하는거 잊지 말기!
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n+1)]

def find_parent(node):
    if parents[node] != node:
        # 여기서 return하는게 아니다! 기억하자!
        parents[node] = find_parent(parents[node])
    return parents[node]

def union_find(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y  

for i in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union_find(a,b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")

'''
https://www.acmicpc.net/board/view/91588
'''