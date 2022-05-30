from collections import deque
n = int(input())
m = int(input())

node = [False] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

# bfs 풀이방법
def bfs(v):
    count = 0
    queue = deque([v])
    node[v] = True
    while queue:
        v = queue.popleft()
        for i in range(1,n+1):
            if graph[v][i] == 1 and not node[i]:
                count += 1
                queue.append(i)
                node[i] = True
    return count

# dfs 풀이방법
def dfs(v):
    node[v] = True
    for i in range(1,n+1):
        if graph[v][i] == 1 and not node[i]:
            dfs(i)


# print(bfs(1))
dfs(1)
result = len([i for i in node if i])
print(result-1)