'''
dfs + dp 문제 (트리 DP)
https://chanhuiseok.github.io/posts/algo-56/
'''

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 초기화, 처음에는 서브노드의 개수는 자기 자신 하나
dp = [1] * (n+1)
visited = [False] * (n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(node):
    visited[node] = True

    for n in graph[node]:
        if not visited[n]:
            # 현재 루트에 하위 서브 노드들의 값을 더해줌
            dp[node] += dfs(n)
    return dp[node]

dfs(r)

for _ in range(q):
    node = int(input())
    print(dp[node])