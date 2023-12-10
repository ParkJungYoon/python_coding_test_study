from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n + 1))
result = []

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))

print("<" + ", ".join(result) + ">")


# 시간 오래걸림. 6524ms

'''
from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n+1))
count = 0
result = []

while queue:
    count += 1
    current = queue.popleft()

    if count % k != 0:
        queue.append(current)
    else:
        result.append(str(current))

print("<" + ", ".join(result) + ">")
'''