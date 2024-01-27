from collections import deque
import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

heapq.heapify(a)

for _ in range(m):
    sum_node = heapq.heappop(a) + heapq.heappop(a)
    heapq.heappush(a, sum_node)
    heapq.heappush(a, sum_node)

print(sum(a))


'''
# 덱큐 왜 시간초과 났는지 꼭 다시 생각해보기.
a.sort()
queue = deque(a)
temp = deque([])

# 시간초과
for _ in range(m):
    sum_node = queue.popleft() + queue.popleft()

    if not queue:
        queue.appendleft(sum_node)
        queue.appendleft(sum_node)
        continue

    while queue:
        if queue[0] >= sum_node:
            break
        temp.append(queue.popleft())
    queue.appendleft(sum_node)
    queue.appendleft(sum_node)
    while temp:
        queue.appendleft(temp.pop())

print(sum(queue))
'''

'''
idx = 0
min_num = 0
sum_node = 0

for _ in range(m):
    if min_num == 0:
        sum_node = a[idx] + a[idx+1]
        min_num += sum_node * 2
        idx += 2
        continue
    if a[idx] + sum_node >= a[idx] + a[idx+1]:
        min_num -= sum_node
        sum_node = a[idx]+sum_node
        min_num += sum_node*2
        idx += 1
    else:
        sum_node 
'''

'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
idx = 0
answer = 0

a.sort()

while idx < m:
    temp = a[idx] + a[idx+1]
    # 새로운 값을 더해주기 전에 기존 값 빼주기
    if idx != 0:
        answer -= a[idx]

    a[idx+1] = temp
    answer += (temp * 2)
    idx += 1

answer += sum(a[idx+1:])

print(answer)
'''