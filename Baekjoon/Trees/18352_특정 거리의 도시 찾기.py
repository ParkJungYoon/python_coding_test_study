import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(node):
    queue = deque([(0, node)])
    visited[node] = True
    result = []

    while queue:
        cost, cur = queue.popleft()
        if cost == k:
            result.append(cur)
        
        for n in graph[cur]:
            if not visited[n]:
                visited[n] = True
                queue.append((cost+1, n))
    return result

answer = bfs(x)

if not answer: print(-1)
answer.sort()
print(*answer, sep="\n")
