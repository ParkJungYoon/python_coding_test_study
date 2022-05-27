from collections import deque
n, k = list(map(int,input().split()))
queue = deque(i for i in range(1,n+1))
result = []
count = 0
while queue:
    for i in list(queue):
        count += 1
        if count == k:
            result.append(str(queue.popleft()))
            count = 0
        else:
            queue.append(queue.popleft())
print('<'+', '.join(result)+'>')