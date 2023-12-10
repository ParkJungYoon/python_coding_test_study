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