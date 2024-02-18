'''
x에서 파티를 하고 다시 자신의 노드로 돌아가야한다. 그 경로가 최소.
'''

import heapq
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end,cost))


def dijkstra(n, distance):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    # n번(시작) 노드까지 가는데 0 비용
    heapq.heappush(q, (0, n))
    distance[n] = 0

    while q: 
    	# 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        cur_cost, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # distance에는 가장 적은 비용 저장 중인데 이미 더 적은거면 해당 노드 안거쳐도 됨.
        if distance[now] < cur_cost:
            continue
        # 현재 노드에 연결된 마을 다 들려봄
        # node = (이동 노드, 비용)
        for node in graph[now]:
            # 거쳐가는 경우
            cost = cur_cost + node[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

# x(파티 장소) 노드에서 각각의 노드로 돌아가는 리스트를 미리 구해둠.
back_home = [sys.maxsize] * (n+1)
dijkstra(x, back_home)

answer = 0
# 하나씩 1번, 2번,... 노드에서 출발했을 때 집에 돌아오는 경로 구함.
for i in range(1, n+1):
    if i == x:
        continue
    distance = [sys.maxsize] * (n+1)
    dijkstra(i, distance)
    # distance[x] : 1번에서 출발한 결과 x 파티까지 최단경로
    # back_home[i] : x번에서 출발한 결과 현재 노드까지 돌아오는 최단경로
    answer = max(answer, distance[x] + back_home[i])

print(answer)