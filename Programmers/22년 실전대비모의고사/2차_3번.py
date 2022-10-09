from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[0] * (n+1) for _ in range(n+1)]

    for road in roads:
        x, y = road
        graph[x][y] = graph[y][x] = 1

    # for i in sources:
    #     bfs(i)
    return answer

def bfs(v):
    queue = deque([v])
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if i == 1:
                graph[cur][i] = graph[cur] + 1
                queue.append(i)
            if i == destination:
                return