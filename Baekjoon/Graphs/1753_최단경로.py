import sys
import heapq
input = sys.stdin.readline

e, v = map(int, input().split())
k = int(input())
graph = [[] for _ in range(e+1)]
dist = [sys.maxsize] * (e+1)
print(graph)

for _ in range(v):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(n):
    temp = []
    # 시작 노드
    heapq.heappush(temp, (0, n))
    dist[n] = 0
    
    while temp:
        cur_cost, cur_n = heapq.heappop(temp)
        if dist[cur_n] < cur_cost:
            continue

        for g in graph[cur_n]:
            new_cost = g[1] + cur_cost
            if new_cost < dist[g[0]]:
                dist[g[0]] = new_cost
                heapq.heappush(temp, (new_cost, g[0]))

dijkstra(k)

for i in range(1, e+1):
    if dist[i] != sys.maxsize:
        print(dist[i])
    else:
        print("INF")