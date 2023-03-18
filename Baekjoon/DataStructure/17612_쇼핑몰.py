import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque([])
counter = []

for i in range(n):
    id, w = map(int, input().split())
    if i < k: 
        heapq.heappush(counter, (w,i+1,id))
        continue
    queue.append((w,id))


time = 0
answer = [0]
while counter:
    time += 1
    temp = []

    while time == counter[0][0]:
        w2, idx, id2 = heapq.heappop(counter)
        temp.append((idx,id2))

        if queue:
            temp1, temp2 = queue.popleft()
            heapq.heappush(counter, (temp1+time,idx,temp2))

        if len(counter) == 0:
            break
    if temp:
    # 동시에 빠져나가는 카트 중 idx가 높은 순으로 나가야함
        temp.sort(reverse=True)
        for tt in temp:
            answer.append(tt[1])

result = 0
for i in range(1,n+1):
    result += i * answer[i]

print(result)

'''
4 2
123 4
111 4
15 2
77 3

[111, 123, 15, 77]
'''