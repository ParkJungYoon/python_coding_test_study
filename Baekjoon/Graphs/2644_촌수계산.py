import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

'''
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent][child] = 1
    graph[child][parent] = 1


def bfs(p1, p2):
    global result
    queue = deque([(p1, 0)])
    visited[p1] = True

    while queue:
        node, count = queue.popleft()
        if node == p2:
            return count
        for i in range(1, n+1):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append((i, count+1))
    return -1            

result = bfs(p1,p2)
print(result)
'''

# dfs풀이
graph = [[] for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent) 

result = []
visited = [False] * (n+1)
def dfs(p1, count):
    count += 1
    visited[p1] = True

    if p1 == p2:
        result.append(count-1)
        return

    for i in graph[p1]:
        if not visited[i]:
            dfs(i, count)


dfs(p1,0)
if not result:
    print(-1)
else:
    print(*result)

'''
input:
9
8 6
8
1 2
1 3
2 7
2 8
2 9
4 5
4 6
9 4

answer: 4
'''