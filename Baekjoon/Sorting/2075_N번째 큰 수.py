import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

'''
N번째 큰 수니깐 값을 일단 넣고
최소힙으로 작은 수 꺼내서 그것보다 크면 큐에 넣고 아니면 빼기
'''

for i in range(n):
    numbers = map(int, input().split())
    if not heap:
        for num in numbers:
            heapq.heappush(heap, num)
    else:
        for num in numbers:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])


'''
graph = [list(map(int, input().split())) for _ in range(n)]
print(graph)
answer = 0
for i in range(n-1,-1,-1):
    current = sorted(graph[i], reverse=True)
    before = sorted(graph[i-1], reverse=True)
    cur_idx = 0
    bef_idx = 0
    if current[cur_idx] > before[bef_idx]:
        answer += 1
        cur_idx += 1
    else:
        answer += 1
        bef_idx += 1
'''