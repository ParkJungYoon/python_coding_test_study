from collections import deque
n, k = list(map(int, input().split()))

queue = deque(range(1, n+1))
result = []

count = 0
while queue:
    count += 1
    node = queue.popleft()
    if count == k:
        result.append(str(node))
        count = 0
        continue
    queue.append(node)

print("<"+ ", ".join(result) + ">")