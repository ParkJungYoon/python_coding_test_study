# 최소 비용 최단 경로 -> 다익스트라
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
 
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def delivery(start):
    temp = []
    heapq.heappush(temp, (0, start))
    distance[start] = 0

    while temp:
        dist, now = heapq.heappop(temp)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 현재 꺼낸 거리 값이 기록된 값보다 크면 이미 방문한 것으로 생각
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 가는게 더 비용이 작다면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(temp, (cost, i[0]))

delivery(1)
print(distance[n])