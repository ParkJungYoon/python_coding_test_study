import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

def bfs(node):
    count = 0
    queue = deque([node])
    visited[node] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
    return count

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    result = 0
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1):
        if not visited[i]:
            result += bfs(i)
            
    print(result)
